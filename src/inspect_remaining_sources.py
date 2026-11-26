import pandas as pd

df = pd.read_csv(
    "data/processed/electricity_generation_clean.csv"
)

world = df[
    df["country"].str.casefold() == "world"
]

latest = world[
    world["year"] == 2025
].iloc[0]

print("OTHER ELECTRICITY GENERATION INDICATORS — 2025")
print("=" * 55)

for column in df.columns:
    if "electricity_twh" in column:
        print(f"{column}: {latest[column]}")