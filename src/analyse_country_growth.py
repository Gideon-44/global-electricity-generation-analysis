
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

# Select data for 2000 and 2025
comparison = df[
    (df["country"].isin(countries)) &
    (df["year"].isin([2000, 2025]))
].copy()

# Keep relevant columns
comparison = comparison[
    [
        "country",
        "year",
        "electricity_generation_twh"
    ]
]

# Reshape data so each country has one row
growth = comparison.pivot(
    index="country",
    columns="year",
    values="electricity_generation_twh"
).reset_index()

# Rename columns
growth.columns.name = None
growth = growth.rename(
    columns={
        2000: "Generation 2000 (TWh)",
        2025: "Generation 2025 (TWh)"
    }
)

# Calculate growth metrics
growth["Increase (TWh)"] = (
    growth["Generation 2025 (TWh)"] -
    growth["Generation 2000 (TWh)"]
)

growth["Growth (%)"] = (
    growth["Increase (TWh)"] /
    growth["Generation 2000 (TWh)"]
) * 100

growth["CAGR (%)"] = (
    (
        growth["Generation 2025 (TWh)"] /
        growth["Generation 2000 (TWh)"]
    ) ** (1 / 25) - 1
) * 100

# Sort by absolute increase
growth = growth.sort_values(
    by="Increase (TWh)",
    ascending=False
)

# Display results
print("\nCOUNTRY ELECTRICITY GENERATION GROWTH: 2000–2025")
print("=" * 75)

print(growth.round(2).to_string(index=False))

# Save results
growth.to_csv(
    "data/processed/country_electricity_growth_2000_2025.csv",
    index=False
)

print("\nResults saved to:")
print("data/processed/country_electricity_growth_2000_2025.csv")
