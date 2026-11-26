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

# Sum renewable technologies
renewable_sources = [
    "solar_electricity_twh",
    "wind_electricity_twh",
    "hydro_electricity_twh",
    "bioenergy_electricity_twh",
]

renewable_sum = latest[renewable_sources].sum()

# Sum low-carbon technologies
low_carbon_sources = renewable_sources + [
    "nuclear_electricity_twh"
]

low_carbon_sum = latest[low_carbon_sources].sum()

# Sum fossil-fuel technologies
fossil_sources = [
    "coal_electricity_twh",
    "gas_electricity_twh",
    "oil_electricity_twh",
]

fossil_sum = latest[fossil_sources].sum()

print("AGGREGATE RECONCILIATION — 2025")
print("=" * 45)

print(
    f"Renewables difference: "
    f"{latest['renewables_electricity_twh'] - renewable_sum:.4f} TWh"
)

print(
    f"Low-carbon difference: "
    f"{latest['low_carbon_electricity_twh'] - low_carbon_sum:.4f} TWh"
)

print(
    f"Fossil-fuel difference: "
    f"{latest['fossil_fuels_electricity_twh'] - fossil_sum:.4f} TWh"
)