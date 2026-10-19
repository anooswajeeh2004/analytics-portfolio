import os
from pathlib import Path
from functools import cache
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from analytics.paths import PROJECT_ROOT


def database_url():
    # محاولة تحميل .env من PROJECT_ROOT أو الصعود مستوى واحد من src/analytics
    env_path_1 = PROJECT_ROOT / ".env"
    env_path_2 = Path(__file__).resolve().parents[1] / ".env"

    if env_path_1.exists():
        load_dotenv(env_path_1)
    elif env_path_2.exists():
        load_dotenv(env_path_2)
    else:
        # إذا لم يُوجد، نحمله بالطريقة الافتراضية
        load_dotenv()

    return os.environ["DATABASE_URL"]


@cache
def get_engine():
    return create_engine(
        database_url().replace("postgresql://", "postgresql+psycopg://", 1)
    )


def query(sql):
    return pd.read_sql(text(sql), get_engine())
