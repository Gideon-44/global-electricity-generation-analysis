import pandas as pd

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

print("COUNTRY DATA COVERAGE")
print("=" * 45)

for country in countries:

    country_data = df[
        df["country"].str.casefold() == country.casefold()
    ]

    latest = country_data[
        country_data["electricity_generation_twh"].notna()
    ]

    if latest.empty:
        print(f"{country}: No generation data found")
    else:
        latest_year = latest["year"].max()

        print(
            f"{country}: Latest year = {latest_year}"
        )