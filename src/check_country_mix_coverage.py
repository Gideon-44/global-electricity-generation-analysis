
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

# Filter relevant records
coverage = df[
    (df["country"].isin(countries)) &
    (df["year"].isin(years))
].copy()

# Display generation data availability
print("\nCOUNTRY ELECTRICITY DATA COVERAGE")
print("=" * 60)

for country in countries:
    print(f"\n{country}")

    country_data = coverage[
        coverage["country"] == country
    ]

    for year in years:
        record = country_data[
            country_data["year"] == year
        ]

        if record.empty:
            print(f"  {year}: No record")
        else:
            value = record["electricity_generation_twh"].iloc[0]

            if pd.isna(value):
                print(f"  {year}: Generation data missing")
            else:
                print(f"  {year}: {value:,.2f} TWh")
