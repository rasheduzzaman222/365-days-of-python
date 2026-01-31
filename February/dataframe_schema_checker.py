import pandas as pd

def check_schema(csv_file, expected_schema):
    df = pd.read_csv(csv_file)
    errors = []

    for column, dtype in expected_schema.items():
        if column not in df.columns:
            errors.append(f"Missing column: {column}")
        elif df[column].dtype != dtype:
            errors.append(f"Column {column} type mismatch")

    return errors


if __name__ == "__main__":
    schema = {"id": "int64", "price": "float64"}
    print(check_schema("data.csv", schema))
