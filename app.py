import os
import pandas as pd

DATA_PATH = "/app/data/Student Performance Factors.csv"

print("=" * 45)
print("TP04 - Docker Data Analysis")
print("=" * 45)

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nFirst five rows:")
print(df.head())

print("\nAnalysis completed successfully!")