from analytics.db import query


def profile_table(table_name: str):
    """
    Profiles a given Olist table by returning its total row count
    and column information.
    """
    # 1. Get total rows
    row_count_df = query(f"SELECT COUNT(*) AS total_rows FROM {table_name};")
    total_rows = row_count_df["total_rows"].iloc[0]

    # 2. Get table columns info
    columns_df = query(f"""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = '{table_name}';
    """)

    print(f"\n==============================")
    print(f" TABLE PROFILE: {table_name.upper()}")
    print(f"==============================")
    print(f"Total Rows: {total_rows}")
    print(f"Total Columns: {len(columns_df)}")
    print("\nColumns & Types:")
    print(columns_df.to_string(index=False))
    print(f"==============================\n")

    return total_rows


if __name__ == "__main__":
    tables = [
        "orders",
        "customers",
        "order_items",
        "order_payments",
        "order_reviews",
        "products",
        "sellers",
        "category_translation",
        "geolocation",
    ]

    for t in tables:
        profile_table(t)
