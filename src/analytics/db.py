import os
from functools import cache
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from analytics.paths import PROJECT_ROOT


def database_url():
    load_dotenv(PROJECT_ROOT / ".env")
    return os.environ["DATABASE_URL"]


@cache
def get_engine():
    return create_engine(
        database_url().replace("postgresql://", "postgresql+psycopg://", 1)
    )


def query(sql):
    return pd.read_sql(text(sql), get_engine())


def execute(sql):
    with get_engine().begin() as connection:
        connection.execute(text(sql))
