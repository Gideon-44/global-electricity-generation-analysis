
import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]

data_path = (
    project_dir
    / "data"
    / "processed"
    / "electricity_generation_clean.csv"
)

df = pd.read_csv(data_path)

world = df[
    df["country"].str.casefold() == "world"
].copy()

columns = [
    "year",
    "electricity_generation_twh",
    "fossil_fuels_electricity_twh",
    "low_carbon_electricity_twh",
]

world = world[
    (world["year"] >= 1915)
    & (world["year"] <= 1922)
]

print("\nGLOBAL ELECTRICITY MIX: HISTORICAL INVESTIGATION")
print("------------------------------------------------")

print(
    world[columns].to_string(index=False)
)
