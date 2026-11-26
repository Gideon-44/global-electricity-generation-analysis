
from pathlib import Path
import pandas as pd

# Locate project and dataset
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "raw" / "owid_energy.csv"

# Load original dataset
df = pd.read_csv(DATA_FILE)

print("=" * 55)
print("ELECTRICITY DATA QUALITY INVESTIGATION")
print("=" * 55)

# 1. Check duplicate location-year records
duplicates = df.duplicated(
    subset=["country", "year"]
).sum()

print("\n1. DUPLICATE RECORDS")
print(f"Duplicate location-year records: {duplicates}")

# 2. Check missing ISO codes
missing_iso = df["iso_code"].isna().sum()

print("\n2. MISSING ISO CODES")
print(f"Records without ISO codes: {missing_iso}")

print("\nExamples of locations without ISO codes:")
print(
    df.loc[df["iso_code"].isna(), "country"]
    .drop_duplicates()
    .head(15)
    .to_list()
)

# 3. Check electricity generation coverage
print("\n3. ELECTRICITY GENERATION COVERAGE")

generation = df["electricity_generation_twh"].dropna()

print(f"Available observations: {len(generation):,}")
print(
    "Earliest year:",
    df.loc[
        df["electricity_generation_twh"].notna(),
        "year"
    ].min()
)
print(
    "Latest year:",
    df.loc[
        df["electricity_generation_twh"].notna(),
        "year"
    ].max()
)

# 4. Check key electricity indicators
indicators = [
    "electricity_generation_twh",
    "renewables_electricity_twh",
    "solar_electricity_twh",
    "wind_electricity_twh",
    "hydro_electricity_twh",
    "coal_electricity_twh",
    "gas_electricity_twh",
]

print("\n4. ELECTRICITY INDICATOR COMPLETENESS")

for column in indicators:
    available = df[column].notna().sum()
    missing = df[column].isna().sum()

    print(
        f"{column}: "
        f"{available:,} available, "
        f"{missing:,} missing"
    )

# 5. Check negative generation values
print("\n5. NEGATIVE GENERATION VALUES")

for column in indicators:
    negative = (df[column] < 0).sum()
    print(f"{column}: {negative} negative values")

# 6. Check data types
print("\n6. DATA TYPES")
print(df[["country", "year", "iso_code"]].dtypes)

# 7. Check most represented locations
print("\n7. MOST REPRESENTED LOCATIONS")
print(df["country"].value_counts().head(10))

print("\nINVESTIGATION COMPLETED!")
