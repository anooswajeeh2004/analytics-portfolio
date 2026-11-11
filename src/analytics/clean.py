import pandas as pd

from analytics.db import execute, get_engine, query
from analytics.schemas import SCHEMAS

RAW_TABLES = [
    "orders",
    "order_items",
    "order_payments",
    "products",
    "category_translation",
    "sellers",
    "customers",
    "order_reviews",
]

KEYS = {
    "orders": ["order_id"],
    "order_items": ["order_id", "order_item_id"],
    "order_payments": ["order_id", "payment_sequential"],
    "products": ["product_id"],
    "sellers": ["seller_id"],
    "customers": ["customer_id"],
}

CITY_FIXES = {
    "sao paulop": "sao paulo",
    "sbc": "sao bernardo do campo",
}

EXTRA_TRANSLATIONS = pd.DataFrame(
    {
        "product_category_name": [
            "pc_gamer",
            "portateis_cozinha_e_preparadores_de_alimentos",
        ],
        "product_category_name_english": [
            "pc_gamer",
            "portable_kitchen_and_food_preparers",
        ],
    }
)


def log_rows(table, rows, column, new_value, action, rule):
    key = rows[KEYS[table][0]].astype(str)
    for key_column in KEYS[table][1:]:
        key = key + "/" + rows[key_column].astype(str)
    return pd.DataFrame(
        {
            "table": table,
            "key": key,
            "column": column,
            "old_value": rows[column].astype(str),
            "new_value": new_value,
            "action": action,
            "rule": rule,
        }
    )


def normalize_city(cities):
    return (
        cities.str.strip()
        .str.lower()
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("ascii")
        .str.replace("'", " ")
        .str.replace(r"\s+", " ", regex=True)
    )


def clean_orders(orders):
    carrier_first = orders["order_delivered_carrier_date"] < orders["order_approved_at"]
    delivered_first = (
        orders["order_delivered_customer_date"] < orders["order_delivered_carrier_date"]
    )
    log = pd.concat(
        [
            log_rows(
                "orders",
                orders[carrier_first],
                "order_delivered_carrier_date",
                "kept, dates_ok = False",
                "flagged",
                "carrier date before approval date",
            ),
            log_rows(
                "orders",
                orders[delivered_first],
                "order_delivered_customer_date",
                "kept, dates_ok = False",
                "flagged",
                "delivery date before carrier date",
            ),
        ]
    )
    orders = orders.assign(dates_ok=~(carrier_first | delivered_first))
    return orders, log


def clean_items(items, orders):
    purchase = items.merge(orders, on="order_id", how="left", validate="many_to_one")[
        "order_purchase_timestamp"
    ]
    far_deadline = (items["shipping_limit_date"] - purchase) > pd.Timedelta(days=365)
    log = log_rows(
        "order_items",
        items[far_deadline],
        "shipping_limit_date",
        "(missing)",
        "changed",
        "shipping deadline more than a year after purchase",
    )
    items = items.assign(
        shipping_limit_date=items["shipping_limit_date"].mask(far_deadline)
    )
    return items, log


def clean_payments(payments):
    no_type = payments["payment_type"] == "not_defined"
    zero_installments = payments["payment_installments"] == 0
    log = pd.concat(
        [
            log_rows(
                "order_payments",
                payments[~no_type],
                "payment_type",
                "(row removed)",
                "removed",
                "no payment type and no money",
            ),
            log_rows(
                "order_payments",
                payments[zero_installments],
                "payment_installments",
                "(missing)",
                "changed",
                "0 installments is impossible",
            ),
        ]
    )
    payments = payments[~no_type].astype({"payment_installments": "Int64"})
    payments = payments.assign(
        payment_installments=payments["payment_installments"].mask(
            payments["payment_installments"] == 0
        )
    )
    return payments, log


def clean_products(products, translation):
    zero_weight = products["product_weight_g"] == 0
    log = log_rows(
        "products",
        products[zero_weight],
        "product_weight_g",
        "(missing)",
        "changed",
        "a weight of 0 g is impossible",
    )
    whole_numbers = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]
    products = products.assign(
        product_weight_g=products["product_weight_g"].mask(zero_weight)
    )
    products = products.astype({column: "Int64" for column in whole_numbers})
    translation = pd.concat([translation, EXTRA_TRANSLATIONS], ignore_index=True)
    products = products.merge(
        translation, on="product_category_name", how="left", validate="many_to_one"
    )
    products = products.assign(
        category=products["product_category_name_english"].fillna("unknown")
    )
    return products, log


def clean_city(table, df, city_column, state_column):
    city = normalize_city(df[city_column])
    city = city.str.split(r" - |[/\\,]", regex=True).str[0].str.strip()
    state = df[state_column].str.lower()
    ends_with_state = (city.str[-3:] == " " + state) | (city.str[-3:] == "-" + state)
    city = city.mask(ends_with_state, city.str[:-3])
    city = city.replace(CITY_FIXES)
    not_a_city = (
        city.str.fullmatch(r"[0-9]+") | city.str.contains("@") | (city == state)
    )
    city = city.mask(not_a_city)
    changed = (city != df[city_column]) & ~not_a_city
    log = pd.concat(
        [
            log_rows(
                table,
                df[changed],
                city_column,
                city[changed],
                "changed",
                "city spelling",
            ),
            log_rows(
                table,
                df[not_a_city],
                city_column,
                "(missing)",
                "changed",
                "not a city name",
            ),
        ]
    )
    df = df.copy()
    df[city_column] = city
    return df, log


def main():
    raw = {table: query(f"SELECT * FROM {table}") for table in RAW_TABLES}

    orders, orders_log = clean_orders(raw["orders"])
    items, items_log = clean_items(raw["order_items"], raw["orders"])
    payments, payments_log = clean_payments(raw["order_payments"])
    products, products_log = clean_products(
        raw["products"], raw["category_translation"]
    )
    sellers, sellers_log = clean_city(
        "sellers", raw["sellers"], "seller_city", "seller_state"
    )
    customers, customers_log = clean_city(
        "customers", raw["customers"], "customer_city", "customer_state"
    )

    clean = {
        "orders": orders,
        "order_items": items,
        "order_payments": payments,
        "products": products,
        "sellers": sellers,
        "customers": customers,
        "order_reviews": raw["order_reviews"],
    }
    log = pd.concat(
        [orders_log, items_log, payments_log, products_log, sellers_log, customers_log],
        ignore_index=True,
    )

    for table, schema in SCHEMAS.items():
        schema.validate(clean[table], lazy=True)

    execute("CREATE SCHEMA IF NOT EXISTS clean")
    for table, df in clean.items():
        df.to_sql(table, get_engine(), schema="clean", if_exists="replace", index=False)
        print(f"{table:<16} raw {len(raw[table]):>9,}   clean {len(df):>9,}")
    log.to_sql(
        "cleaning_log", get_engine(), schema="clean", if_exists="replace", index=False
    )
    counts = log.groupby(["table", "action", "rule"]).size()
    for (table, action, rule), rows in counts.items():
        print(f"{table:<16} {action:<8} {rows:>5}  {rule}")


if __name__ == "__main__":
    main()
