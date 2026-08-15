import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/Amazon Sale Report.csv")


def extract_sales_data():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE, low_memory=False)
    print(f"Extracted {len(df):,} rows")
    print(f"Columns: {list(df.columns)}")
    return df


if __name__ == "__main__":
    extract_sales_data()
