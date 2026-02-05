import pandas as pd

def detect_anomalies(csv_file, column, threshold=3):
    df = pd.read_csv(csv_file)
    mean = df[column].mean()
    std = df[column].std()

    df["z_score"] = (df[column] - mean) / std
    return df[df["z_score"].abs() > threshold]


if __name__ == "__main__":
    print(detect_anomalies("data.csv", "value"))
