import pandas as pd


def detect_anomalies(df):

    if df is None:
        return []

    anomalies = []

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:

        mean = df[col].mean()
        std = df[col].std()

        upper = mean + 3 * std
        lower = mean - 3 * std

        outliers = df[(df[col] > upper) | (df[col] < lower)]

        if not outliers.empty:
            anomalies.append({
                "column": col,
                "count": len(outliers)
            })

    print(f"⚠️ Found {len(anomalies)} anomaly columns")

    return anomalies