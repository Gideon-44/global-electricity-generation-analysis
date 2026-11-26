import pandas as pd

df = pd.read_csv(
    "data/processed/electricity_generation_clean.csv"
)

world = df[
    df["country"].str.casefold() == "world"
].copy()

latest = world[
    world["year"] == 2025
].iloc[0]

source_columns = [
    "coal_electricity_twh",
    "gas_electricity_twh",
    "oil_electricity_twh",
    "hydro_electricity_twh",
    "nuclear_electricity_twh",
    "solar_electricity_twh",
    "wind_electricity_twh",
    "bioenergy_electricity_twh",
]

source_total = latest[source_columns].sum()

total_generation = latest[
    "electricity_generation_twh"
]

difference = total_generation - source_total

print("GLOBAL ELECTRICITY GENERATION BALANCE — 2025")
print("=" * 50)

print(f"Total generation: {total_generation:,.2f} TWh")
print(f"Sum of listed sources: {source_total:,.2f} TWh")
print(f"Difference: {difference:,.2f} TWh")

print("\nIndividual source values:")

for column in source_columns:
    print(f"{column}: {latest[column]:,.2f} TWh")