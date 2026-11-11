import pandera.pandas as pa

ORDER_STATUSES = [
    "delivered",
    "shipped",
    "canceled",
    "unavailable",
    "invoiced",
    "processing",
    "created",
    "approved",
]
PAYMENT_TYPES = ["credit_card", "boleto", "voucher", "debit_card"]

orders_schema = pa.DataFrameSchema(
    {
        "order_id": pa.Column(str, unique=True),
        "order_status": pa.Column(str, pa.Check.isin(ORDER_STATUSES)),
        "dates_ok": pa.Column(bool),
    },
    checks=[
        pa.Check(
            lambda df: (
                ~(
                    df["dates_ok"]
                    & (df["order_delivered_carrier_date"] < df["order_approved_at"])
                )
            ),
            name="carrier date not before approval date",
        ),
        pa.Check(
            lambda df: (
                ~(
                    df["dates_ok"]
                    & (
                        df["order_delivered_customer_date"]
                        < df["order_delivered_carrier_date"]
                    )
                )
            ),
            name="delivery date not before carrier date",
        ),
    ],
)

payments_schema = pa.DataFrameSchema(
    {
        "payment_type": pa.Column(str, pa.Check.isin(PAYMENT_TYPES)),
        "payment_installments": pa.Column("Int64", pa.Check.ge(1), nullable=True),
        "payment_value": pa.Column(float, pa.Check.ge(0)),
    },
    unique=["order_id", "payment_sequential"],
)

# Exercise 3.a
# This schema validates the `products` table by ensuring `product_id` is a unique string, `product_weight_g` is a positive integer (allowing missing values), and `category` is a non-null string field.

products_schema = pa.DataFrameSchema(
    {
        "product_id": pa.Column(str, unique=True),
        "product_weight_g": pa.Column("Int64", pa.Check.gt(0), nullable=True),
        "category": pa.Column(str, nullable=False),
    }
)

# Exercise 3.b
# This schema enforces data integrity on `order_items` by ensuring the primary key pair (`order_id`, `order_item_id`) is strictly unique, unit prices are strictly positive (> 0), and freight charges are non-negative (>= 0).

items_schema = pa.DataFrameSchema(
    {
        "price": pa.Column(float, pa.Check.gt(0)),
        "freight_value": pa.Column(float, pa.Check.ge(0)),
    },
    unique=["order_id", "order_item_id"],
)
# Exercise 3.c
# This schema validates the `sellers` table, confirming unique seller identifiers and enforcing strict string checks on `seller_city` to prevent numeric-only strings or invalid characters like `@` while permitting null entries.

sellers_schema = pa.DataFrameSchema(
    {
        "seller_id": pa.Column(str, unique=True),
        "seller_city": pa.Column(
            str,
            checks=[
                pa.Check(
                    lambda city: ~city.dropna().str.fullmatch(r"[0-9]+"),
                    name="no digits only",
                ),
                pa.Check(lambda city: ~city.dropna().str.contains("@"), name="no @"),
            ],
            nullable=True,
        ),
    }
)
SCHEMAS = {
    "orders": orders_schema,
    "order_payments": payments_schema,
    "products": products_schema,
    "order_items": items_schema,
    "sellers": sellers_schema,
}


# This file defines data validation schemas using the `pandera` library for cleaned tables like `orders` and `order_payments`. It enforces strict constraints on data types, allowed categorical values, uniqueness, and logical date sequencing, ensuring that any data corruption halts the pipeline execution before writing to the database.
