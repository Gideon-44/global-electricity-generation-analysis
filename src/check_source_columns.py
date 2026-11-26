import pandas as pd

df = pd.read_csv(
    "data/processed/electricity_generation_clean.csv"
)

for column in df.columns:
    if "bio" in column.lower() or "electricity" in column.lower():
        print(column)