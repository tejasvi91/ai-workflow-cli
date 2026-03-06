import pandas as pd


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Loaded dataset with {len(df)} rows and {len(df.columns)} columns")
        return df
    except Exception as e:
        print("❌ Error loading dataset:", e)
        return None