import pandas as pd

#1. Basic preprocessing (optional)

def preprocess_data(df):
    df = df.drop_duplicates()
    return df

# 2. Create LTV (TARGET VARIABLE)

def create_ltv(df):
    df["LTV"] = (
        df["Purchase Amount (USD)"] *
        df["Frequency of Purchases"] *
        df["Previous Purchases"]
    ) * (1 + 0.1 * df["Review Rating"]) * (1 + 0.2 * df["Subscription Status"])

    return df

# 3. Full processing pipeline

def process_pipeline(df):
    df = preprocess_data(df)
    df = create_ltv(df)

    return df