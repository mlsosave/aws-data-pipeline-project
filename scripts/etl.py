import pandas as pd

def extract():
    data = {"id": [1,2,3], "value": [10,20,30]}
    return pd.DataFrame(data)

def transform(df):
    df["value"] = df["value"] * 2
    return df

def load(df):
    print("Loaded data:")
    print(df)

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
