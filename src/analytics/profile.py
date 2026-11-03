import pandas as pd
from analytics.db import query


def profile_table(table_name: str) -> pd.DataFrame:
    """Return one row for each column of the table, with its type, nulls, null_pct, distinct, min and max."""
    columns = query(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
        ORDER BY ordinal_position
    """)

    rows = []
    for column, data_type in zip(columns["column_name"], columns["data_type"]):
        stats = query(f"""
            SELECT
                COUNT(*) - COUNT({column}) AS nulls,
                ROUND(100.0 * (COUNT(*) - COUNT({column})) / COUNT(*), 1) AS null_pct,
                COUNT(DISTINCT {column}) AS "distinct",
                MIN({column})::text AS min,
                MAX({column})::text AS max
            FROM {table_name}
        """)
        rows.append({"column": column, "type": data_type, **stats.iloc[0].to_dict()})

    return pd.DataFrame(rows)
