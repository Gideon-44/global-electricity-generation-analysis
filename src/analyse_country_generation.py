import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "data/processed/electricity_generation_clean.csv"
)

# Countries to compare
countries = [
    "China",
    "United States",
    "India",
    "Germany",
    "Kenya"
]

# Select country records
comparison = df[
    df["country"].isin(countries)
].copy()

# Keep records with total electricity generation
comparison = comparison[
    comparison["electricity_generation_twh"].notna()
]

# Select 2025 data
comparison_2025 = comparison[
    comparison["year"] == 2025
].copy()

# Select relevant columns
comparison_2025 = comparison_2025[
    ["country", "electricity_generation_twh"]
]

# Sort from highest to lowest generation
comparison_2025 = comparison_2025.sort_values(
    by="electricity_generation_twh",
    ascending=False
)

# Rename columns
comparison_2025.columns = [
    "Country",
    "Electricity generation (TWh)"
]

print("\nCOUNTRY ELECTRICITY GENERATION — 2025")
print("=" * 55)

print(
    comparison_2025.round(2).to_string(index=False)
)

# Save results
comparison_2025.to_csv(
    "data/processed/country_generation_2025.csv",
    index=False
)

print("\nResults saved to:")
print("data/processed/country_generation_2025.csv")