import pandas as pd


def transform_sales_data(df):
    df = df.copy()

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # Remove unwanted column
    if "unnamed:_22" in df.columns:
        df = df.drop(columns=["unnamed:_22"])

    # IMPORTANT:
    # Original Amazon CSV date format = MM-DD-YY
    df["date"] = pd.to_datetime(
        df["date"],
        format="%m-%d-%y",
        errors="coerce"
    )

    # Numeric columns
    df["qty"] = pd.to_numeric(
        df["qty"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    # Text columns
    text_columns = [
        "order_id",
        "status",
        "fulfilment",
        "sales_channel",
        "ship_service_level",
        "style",
        "sku",
        "category",
        "size",
        "asin",
        "courier_status",
        "currency",
        "ship_city",
        "ship_state",
        "ship_country",
        "promotion_ids",
        "fulfilled_by"
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()

    # Postal code
    df["ship_postal_code"] = (
        pd.to_numeric(
            df["ship_postal_code"],
            errors="coerce"
        )
        .fillna(0)
        .astype(int)
        .astype(str)
    )

    # B2B
    df["b2b"] = (
        df["b2b"]
        .astype(str)
        .str.lower()
        .map({
            "true": True,
            "false": False
        })
        .fillna(False)
    )

    # Final columns
    final_columns = [
        "index",
        "order_id",
        "date",
        "status",
        "fulfilment",
        "sales_channel",
        "ship_service_level",
        "style",
        "sku",
        "category",
        "size",
        "asin",
        "courier_status",
        "qty",
        "currency",
        "amount",
        "ship_city",
        "ship_state",
        "ship_postal_code",
        "ship_country",
        "promotion_ids",
        "b2b",
        "fulfilled_by"
    ]

    df = df[final_columns]

    return df