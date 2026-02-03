import pandas as pd

def remove_duplicates(csv_file, subset=None):
    df = pd.read_csv(csv_file)
    return df.drop_duplicates(subset=subset)


if __name__ == "__main__":
    print(remove_duplicates("data.csv").head())
