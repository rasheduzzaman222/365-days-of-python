import pandas as pd

def profile_columns(csv_file):
    df = pd.read_csv(csv_file)
    profile = {}

    for col in df.columns:
        profile[col] = {
            "dtype": str(df[col].dtype),
            "missing": int(df[col].isnull().sum()),
            "unique": int(df[col].nunique())
        }

    return profile


if __name__ == "__main__":
    print(profile_columns("data.csv"))
