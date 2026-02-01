import pandas as pd

def handle_missing_values(csv_file):
    df = pd.read_csv(csv_file)

    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    df = df.dropna(subset=df.columns.difference(numeric_cols))
    return df


if __name__ == "__main__":
    print(handle_missing_values("data.csv").head())
