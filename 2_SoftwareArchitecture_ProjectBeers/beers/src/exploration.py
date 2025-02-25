import pandas as pd

# Explore the data
def explore_data(df):
    print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
    print(f"Dataset contains {df.isnull().sum().sum()} missing values.")
    print(f"Dataset contains {df.duplicated().sum()} duplicated rows.")

