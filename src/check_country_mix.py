
import pandas as pd

# Load country electricity mix results
df = pd.read_csv(
    "data/processed/country_electricity_mix_2025.csv"
)

# Calculate the total of the three non-overlapping categories
df["Calculated total (%)"] = (
    df["Renewables (%)"] +
    df["Fossil fuels (%)"] +
    df["Nuclear (%)"]
)

print("\nCOUNTRY ELECTRICITY MIX QUALITY CHECK")
print("=" * 55)

print(
    df[
        [
            "Country",
            "Calculated total (%)"
        ]
    ].round(2).to_string(index=False)
)

# Check that each country's mix adds up to approximately 100%
assert (
    (df["Calculated total (%)"] - 100).abs() < 0.1
).all(), "Some country electricity mixes do not add up to 100%."

print("\nAll country electricity mixes add up to approximately 100%.")
