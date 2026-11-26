
from pathlib import Path
import pandas as pd

# ----------------------------------------
# 1. DEFINE PROJECT PATHS
# ----------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

RAW_FILE = PROJECT_DIR / "data" / "raw" / "owid_energy.csv"

PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

OUTPUT_FILE = PROCESSED_DIR / "electricity_generation_clean.csv"


# ----------------------------------------
# 2. DEFINE IMPORTANT COLUMNS
# ----------------------------------------

GENERATION_COLUMNS = [
    "electricity_generation_twh",
    "renewables_electricity_twh",
    "low_carbon_electricity_twh",
    "fossil_fuels_electricity_twh",
    "solar_electricity_twh",
    "wind_electricity_twh",
    "hydro_electricity_twh",
    "coal_electricity_twh",
    "gas_electricity_twh",
    "oil_electricity_twh",
    "nuclear_electricity_twh",
    "bioenergy_electricity_twh",
    "other_renewables_excluding_bioenergy_electricity_twh",
]

REQUIRED_COLUMNS = [
    "country",
    "year",
    "iso_code",
] + GENERATION_COLUMNS


# ----------------------------------------
# 3. LOAD AND CLEAN DATA
# ----------------------------------------

def clean_dataset():

    print("Starting electricity data cleaning...")

    # Load original data
    df = pd.read_csv(RAW_FILE)

    original_rows = len(df)

    print(f"Original records: {original_rows:,}")

    # Check required columns exist
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Keep only the columns needed for this analysis
    df = df[REQUIRED_COLUMNS].copy()

    # Standardise country names and ISO codes
    df["country"] = df["country"].str.strip()

    df["iso_code"] = (
        df["iso_code"]
        .str.strip()
        .str.upper()
    )

    # Ensure year is numeric
    df["year"] = pd.to_numeric(
        df["year"],
        errors="coerce"
    )

    # Remove records without a usable country name or year
    df = df.dropna(
        subset=["country", "year"]
    ).copy()

    # Keep integer years
    df = df[df["year"] % 1 == 0].copy()
    df["year"] = df["year"].astype("int64")

    # ----------------------------------------
   
    # ----------------------------------------
    # 4. SELECT COUNTRY-LEVEL RECORDS
    # ----------------------------------------

    # Retain three-letter ISO-coded entities
    # and preserve the World aggregate.

    valid_iso = df["iso_code"].str.fullmatch(
        r"[A-Z]{3}",
        na=False
    )

    is_world = df["country"].str.casefold().eq("world")

    df = df[valid_iso | is_world].copy()

    # ----------------------------------------
    # 5. PRESERVE USEFUL GENERATION RECORDS
    # ----------------------------------------

    # Keep records with at least one available
    # electricity generation indicator.

    has_generation_data = (
        df[GENERATION_COLUMNS]
        .notna()
        .any(axis=1)
    )

    df = df[has_generation_data].copy()


    # ----------------------------------------
    # 6. CHECK DUPLICATES
    # ----------------------------------------

    duplicate_count = df.duplicated(
        subset=["iso_code", "year"]
    ).sum()

    if duplicate_count > 0:
        raise ValueError(
            f"Found {duplicate_count} duplicate country-year records."
        )

    # ----------------------------------------
    # 7. CHECK NEGATIVE GENERATION VALUES
    # ----------------------------------------

    negative_counts = (
        df[GENERATION_COLUMNS] < 0
    ).sum()

    if negative_counts.any():
        print("WARNING: Negative generation values detected.")
        print(negative_counts[negative_counts > 0])

    # ----------------------------------------
    # 8. SAVE PROCESSED DATA
    # ----------------------------------------

    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    df = df.sort_values(
        ["country", "year"]
    ).reset_index(drop=True)

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    # ----------------------------------------
    # 9. PRINT CLEANING SUMMARY
    # ----------------------------------------

    print("\nCLEANING COMPLETED!")
    print("------------------------------")

    print(f"Original records: {original_rows:,}")
    print(f"Processed records: {len(df):,}")
    print(f"Records removed: {original_rows - len(df):,}")

    print(
        "Unique countries:",
        df["iso_code"].nunique()
    )

    print(
        "Year range:",
        df["year"].min(),
        "-",
        df["year"].max()
    )

    print(
        "Duplicate records:",
        df.duplicated(
            subset=["iso_code", "year"]
        ).sum()
    )

    print(
        "Output saved to:",
        OUTPUT_FILE
    )


if __name__ == "__main__":
    clean_dataset()
