import pandas as pd

# Load the cleaned electricity dataset
df = pd.read_csv(
    "data/processed/electricity_generation_clean.csv"
)

# Select global records
world = df[df["country"].str.casefold() == "world"].copy()

# Set the comparison years
start_year = 2000
end_year = 2025
number_of_years = end_year - start_year

# Electricity generation columns to analyse
sources = {
    "Total electricity": "electricity_generation_twh",
    "Coal": "coal_electricity_twh",
    "Gas": "gas_electricity_twh",
    "Oil": "oil_electricity_twh",
    "Hydro": "hydro_electricity_twh",
    "Nuclear": "nuclear_electricity_twh",
    "Solar": "solar_electricity_twh",
    "Wind": "wind_electricity_twh",
    "Bioenergy": "bioenergy_electricity_twh",
    "Other renewables": "other_renewables_excluding_bioenergy_electricity_twh",
}

# Get the records for the comparison years
start_data = world[world["year"] == start_year]
end_data = world[world["year"] == end_year]

if start_data.empty or end_data.empty:
    raise ValueError("The comparison year is missing from the World data.")

start_data = start_data.iloc[0]
end_data = end_data.iloc[0]

print(f"\nGLOBAL ELECTRICITY GENERATION: {start_year}–{end_year}")
print("=" * 65)

results = []

for source_name, column in sources.items():

    start_value = start_data[column]
    end_value = end_data[column]

    # Skip calculations if either value is missing
    if pd.isna(start_value) or pd.isna(end_value):
        print(f"\n{source_name}: Missing data for one or both years.")
        continue

    # Calculate percentage growth
    if start_value > 0:
        percentage_growth = (
            (end_value - start_value) / start_value
        ) * 100

        # Calculate compound annual growth rate
        cagr = (
            (end_value / start_value) ** (1 / number_of_years) - 1
        ) * 100
    else:
        percentage_growth = None
        cagr = None

    # Calculate share of total generation in the end year
    total_generation = end_data["electricity_generation_twh"]

    share_2025 = (end_value / total_generation) * 100

    results.append({
        "Source": source_name,
        "2000 (TWh)": start_value,
        "2025 (TWh)": end_value,
        "Growth (%)": percentage_growth,
        "CAGR (%)": cagr,
        "2025 Share (%)": share_2025,
    })

# Display the results
results_df = pd.DataFrame(results)

print(
    results_df.round(2).to_string(index=False)
)

# Save the results
results_df.to_csv(
    "data/processed/electricity_source_growth.csv",
    index=False
)

print("\nResults saved to:")
print("data/processed/electricity_source_growth.csv")