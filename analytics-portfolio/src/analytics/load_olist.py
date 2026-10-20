import psycopg
from pathlib import Path
from analytics.db import database_url
from analytics.paths import PROJECT_ROOT, RAW_OLIST

FILES = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}


def main():
    create_tables = (
        Path(__file__).resolve().parent.parent.parent / "sql" / "create_tables.sql"
    ).read_text(encoding="utf-8")
    with psycopg.connect(database_url()) as conn:
        conn.execute(create_tables)
        for table, file_name in FILES.items():
            with open(RAW_OLIST / file_name, "rb") as source:
                with conn.cursor().copy(
                    f"COPY {table} FROM STDIN WITH (FORMAT csv, HEADER true)"
                ) as copy:
                    while chunk := source.read(1024 * 1024):
                        copy.write(chunk)
            rows = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"{table:<22} {rows:>10}")


if __name__ == "__main__":
    main()
