
from pathlib import Path
import pandas as pd

# Locate the downloaded dataset
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "owid_energy.csv"

# Load dataset
df = pd.read_csv(DATA_FILE)

# 1. Dataset dimensions
print("\n--- DATASET DIMENSIONS ---")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

# 2. First five records
print("\n--- FIRST FIVE RECORDS ---")
print(df.head())

# 3. Column names
print("\n--- ALL COLUMN NAMES ---")
for column in df.columns:
    print(column)

# 4. Electricity-related columns
print("\n--- ELECTRICITY COLUMNS ---")
electricity_columns = [
    column for column in df.columns
    if "electricity" in column.lower()
]

for column in electricity_columns:
    print(column)

# 5. Missing values
print("\n--- MISSING VALUES ---")
print(
    df.isnull().sum()
    .sort_values(ascending=False)
    .head(15)
)

# 6. Country and year coverage
print("\n--- COUNTRY AND YEAR COVERAGE ---")
print("Countries/locations:", df["country"].nunique())
print("First year:", df["year"].min())
print("Last year:", df["year"].max())

print("\nDATASET INSPECTION COMPLETED!")
