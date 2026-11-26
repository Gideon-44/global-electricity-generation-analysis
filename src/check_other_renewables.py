import pandas as pd

df = pd.read_csv(
    "data/raw/owid_energy.csv"
)

world = df[
    df["country"].str.casefold() == "world"
]

latest = world[
    world["year"] == 2025
].iloc[0]

columns = [
    "other_renewables_excluding_bioenergy_electricity_twh",
    "other_renewables_including_bioenergy_electricity_twh",
    "renewables_electricity_twh",
    "low_carbon_electricity_twh",
]

print("OTHER RENEWABLES — GLOBAL, 2025")
print("=" * 50)

for column in columns:
    print(f"{column}: {latest[column]} TWh")