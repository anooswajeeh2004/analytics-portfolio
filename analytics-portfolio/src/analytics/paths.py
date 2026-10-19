from pathlib import Path

# الصعود مستويين من src/analytics للوصول إلى مجلد analytics-portfolio الرئيسي
PROJECT_ROOT = Path(__file__).resolve().parents[3]

RAW_OLIST = PROJECT_ROOT / "data" / "raw" / "olist"
PROCESSED = PROJECT_ROOT / "data" / "processed"
