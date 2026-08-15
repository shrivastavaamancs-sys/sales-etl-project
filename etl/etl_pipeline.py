from pathlib import Path
import sys

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.extract import extract_sales_data
from src.transform import transform_sales_data


OUTPUT_FILE = Path("data/processed/sales_cleaned.csv")


def run_pipeline():
    print("=" * 60)
    print("SALES ETL PIPELINE")
    print("=" * 60)

    # Extract
    df = extract_sales_data()

    # Transform
    df_clean = transform_sales_data(df)

    # Load
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(OUTPUT_FILE, index=False)

    print(f"Loaded cleaned data to: {OUTPUT_FILE}")
    print(f"Final row count: {len(df_clean):,}")
    print("=" * 60)
    print("ETL PIPELINE COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
