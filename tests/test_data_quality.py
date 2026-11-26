
import pandas as pd
from pathlib import Path

# Load the cleaned dataset
DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "processed"
    / "electricity_generation_clean.csv"
)

df = pd.read_csv(DATA_PATH)

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
]


def test_required_columns_exist():
    required = ["country", "year", "iso_code"] + GENERATION_COLUMNS
    assert set(required).issubset(df.columns)


def test_country_names_are_present():
    assert df["country"].notna().all()
    assert df["country"].str.strip().ne("").all()


def test_years_are_valid_integers():
    assert pd.api.types.is_integer_dtype(df["year"])
    assert df["year"].between(1700, 2025).all()


def test_iso_codes_are_valid_for_entity_type():
    is_world = df["country"].str.casefold().eq("world")

    assert df.loc[~is_world, "iso_code"].notna().all()
    assert df.loc[~is_world, "iso_code"].str.fullmatch(
        r"[A-Z]{3}"
    ).all()

    assert df.loc[is_world, "iso_code"].isna().all()


def test_no_duplicate_country_year_records():
    assert not df.duplicated(
        subset=["iso_code", "year"]
    ).any()


def test_generation_values_are_not_negative():
    for column in GENERATION_COLUMNS:
        values = df[column].dropna()
        assert (values >= 0).all(), f"Negative values in {column}"


def test_each_record_has_generation_data():
    assert df[GENERATION_COLUMNS].notna().any(axis=1).all()

def test_country_electricity_mix_sums_to_100():
    mix = pd.read_csv(
        "data/processed/country_electricity_mix_2025.csv"
    )

    calculated_total = (
        mix["Renewables (%)"] +
        mix["Fossil fuels (%)"] +
        mix["Nuclear (%)"]
    )

    assert (
        (calculated_total - 100).abs() < 0.1
    ).all()
