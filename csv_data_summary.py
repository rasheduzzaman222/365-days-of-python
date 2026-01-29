import pandas as pd

def summarize_csv(file_path):
    df = pd.read_csv(file_path)

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }

    return summary


if __name__ == "__main__":
    print(summarize_csv("data.csv"))
