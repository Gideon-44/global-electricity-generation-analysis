
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

years = [2000, 2025]

# Filter selected countries and years
comparison = df[
    (df["country"].isin(countries)) &
    (df["year"].isin(years))
].copy()

# Select relevant columns
columns = [
    "country",
    "year",
    "electricity_generation_twh",
    "renewables_electricity_twh",
    "fossil_fuels_electricity_twh",
    "nuclear_electricity_twh"
]

comparison = comparison[columns].copy()

# Check for missing values
if comparison[columns[2:]].isna().any().any():
    raise ValueError(
        "Missing generation values found. "
        "Investigate before calculating electricity shares."
    )

# Calculate generation shares
comparison["Renewables (%)"] = (
    comparison["renewables_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

comparison["Fossil fuels (%)"] = (
    comparison["fossil_fuels_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

comparison["Nuclear (%)"] = (
    comparison["nuclear_electricity_twh"] /
    comparison["electricity_generation_twh"]
) * 100

# Check that shares add up to approximately 100%
comparison["Share total (%)"] = (
    comparison["Renewables (%)"] +
    comparison["Fossil fuels (%)"] +
    comparison["Nuclear (%)"]
)

assert (
    (comparison["Share total (%)"] - 100).abs() < 0.1
).all(), "Some electricity mixes do not add up to 100%."

# Keep final output columns
results = comparison[
    [
        "country",
        "year",
        "Renewables (%)",
        "Fossil fuels (%)",
        "Nuclear (%)"
    ]
].copy()

# Sort results
results = results.sort_values(
    by=["country", "year"]
)

# Display results
print("\nCOUNTRY ELECTRICITY MIX CHANGE: 2000 VS 2025")
print("=" * 75)

print(results.round(2).to_string(index=False))

# Save results
results.to_csv(
    "data/processed/country_electricity_mix_change.csv",
    index=False
)

print("\nResults saved to:")
print("data/processed/country_electricity_mix_change.csv")
