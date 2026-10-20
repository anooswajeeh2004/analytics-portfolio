import pandas as pd
from analytics.db import query
from analytics.load_olist import FILES


def table_row_counts() -> pd.DataFrame:
    """إرجاع عدد الصفوف لكل جدول في قاعدة البيانات في شكل DataFrame"""
    results = []
    for table_name in FILES.keys():
        df = query(f"SELECT COUNT(*) as row_count FROM {table_name}")
        count = df["row_count"].iloc[0]
        results.append({"table": table_name, "rows": count})

    return pd.DataFrame(results)
