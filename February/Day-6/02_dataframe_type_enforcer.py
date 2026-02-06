import pandas as pd

def enforce_types(csv_file, schema):
    df = pd.read_csv(csv_file)

    for column, dtype in schema.items():
        if column in df.columns:
            df[column] = df[column].astype(dtype)

    return df


if __name__ == "__main__":
    schema = {"id": "int64", "amount": "float64"}
    print(enforce_types("data.csv", schema).dtypes)
