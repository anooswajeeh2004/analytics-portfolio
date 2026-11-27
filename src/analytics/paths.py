from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_OLIST = PROJECT_ROOT / "data" / "raw" / "olist"
PROCESSED = PROJECT_ROOT / "data" / "processed"
RAW_WEB = PROJECT_ROOT / "data" / "raw" / "web"
RAW_AB = PROJECT_ROOT / "data" / "raw" / "ab_test"
FIGURES = PROJECT_ROOT / "reports" / "figures"
