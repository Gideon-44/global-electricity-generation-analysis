
import pandas as pd
from pathlib import Path

# ----------------------------------------
# 1. LOAD DATA
# ----------------------------------------

project_dir = Path(__file__).resolve().parents[1]

data_path = (
    project_dir
    / "data"
    / "processed"
    / "electricity_generation_clean.csv"
)

df = pd.read_csv(data_path)

# ----------------------------------------
# 2. SELECT WORLD RECORDS
# ----------------------------------------

world = df[
    df["country"].str.casefold() == "world"
].copy()

world = world[
    world["year"].between(1915, 1922)
].sort_values("year")

# ----------------------------------------
# 3. SELECT INDIVIDUAL SOURCES
# ----------------------------------------

source_columns = [
    "year",
    "electricity_generation_twh",
    "coal_electricity_twh",
    "gas_electricity_twh",
    "oil_electricity_twh",
    "hydro_electricity_twh",
    "nuclear_electricity_twh",
    "solar_electricity_twh",
    "wind_electricity_twh",
    "bioenergy_electricity_twh",
]

# ----------------------------------------
# 4. DISPLAY SOURCE GENERATION
# ----------------------------------------

print("\nGLOBAL ELECTRICITY SOURCES: 1915–1922")
print("--------------------------------------")

print(
    world[source_columns].to_string(index=False)
)
