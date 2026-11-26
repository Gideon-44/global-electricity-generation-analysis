import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "data/processed/electricity_generation_clean.csv"
)

countries = [
    "China",
    "United States",
    "India",
    "Germany",
    "Kenya"
]

# Filter 2025 country records
comparison = df[
    (df["country"].isin(countries)) &
    (df["year"] == 2025)
].copy()

# Select relevant columns
columns = [
    "country",
    "electricity_generation_twh",
    "renewables_electricity_twh",
    "low_carbon_electricity_twh",
    "fossil_fuels_electricity_twh",
    "nuclear_electricity_twh"
]

comparison = comparison[columns].copy()

# Calculate generation shares
comparison["Renewables share (%)"] = (
    comparison["renewables_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

comparison["Fossil share (%)"] = (
    comparison["fossil_fuels_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

comparison["Low-carbon share (%)"] = (
    comparison["low_carbon_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

comparison["Nuclear share (%)"] = (
    comparison["nuclear_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

# Select final comparison columns
results = comparison[
    [
        "country",
        "Renewables share (%)",
        "Fossil share (%)",
        "Low-carbon share (%)",
        "Nuclear share (%)"
    ]
].copy()

# Sort by renewable share
results = results.sort_values(
    by="Renewables share (%)",
    ascending=False
)

results.columns = [
    "Country",
    "Renewables (%)",
    "Fossil fuels (%)",
    "Low carbon (%)",
    "Nuclear (%)"
]

print("\nCOUNTRY ELECTRICITY MIX — 2025")
print("=" * 65)

print(results.round(2).to_string(index=False))

# Save results
results.to_csv(
    "data/processed/country_electricity_mix_2025.csv",
    index=False
)

print("\nResults saved to:")
print("data/processed/country_electricity_mix_2025.csv")