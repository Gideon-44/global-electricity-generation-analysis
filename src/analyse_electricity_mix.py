
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------------------
# 1. LOAD THE PROCESSED DATA
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
# 2. SELECT GLOBAL ELECTRICITY DATA
# ----------------------------------------

world = df[
    df["country"].str.casefold() == "world"
].copy()

# Keep records with all three indicators
required_columns = [
    "electricity_generation_twh",
    "fossil_fuels_electricity_twh",
    "low_carbon_electricity_twh"
]

world = world.dropna(subset=required_columns)

world = world.sort_values("year")

# ----------------------------------------
# 3. CALCULATE ELECTRICITY SHARES
# ----------------------------------------

world["fossil_share_percent"] = (
    world["fossil_fuels_electricity_twh"]
    / world["electricity_generation_twh"]
) * 100

world["low_carbon_share_percent"] = (
    world["low_carbon_electricity_twh"]
    / world["electricity_generation_twh"]
) * 100

# ----------------------------------------
# 4. DISPLAY LATEST FINDINGS
# ----------------------------------------

latest = world.iloc[-1]

print("\nGLOBAL ELECTRICITY MIX")
print("----------------------")

print("Latest available year:", int(latest["year"]))

print(
    "Total electricity generation:",
    round(latest["electricity_generation_twh"], 2),
    "TWh"
)

print(
    "Fossil fuel generation:",
    round(latest["fossil_fuels_electricity_twh"], 2),
    "TWh"
)

print(
    "Low-carbon generation:",
    round(latest["low_carbon_electricity_twh"], 2),
    "TWh"
)

print(
    "Fossil fuel share:",
    round(latest["fossil_share_percent"], 2),
    "%"
)

print(
    "Low-carbon share:",
    round(latest["low_carbon_share_percent"], 2),
    "%"
)

# ----------------------------------------
# 5. CREATE THE ELECTRICITY MIX CHART
# ----------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    world["year"],
    world["fossil_share_percent"],
    label="Fossil fuels",
    linewidth=2
)

plt.plot(
    world["year"],
    world["low_carbon_share_percent"],
    label="Low-carbon electricity",
    linewidth=2
)

plt.title(
    "Global Electricity Mix Over Time",
    fontsize=16
)

plt.xlabel("Year", fontsize=12)

plt.ylabel(
    "Share of Total Electricity Generation (%)",
    fontsize=12
)

plt.legend()

plt.grid(True, alpha=0.3)

# ----------------------------------------
# 6. ADD SOURCE INFORMATION
# ----------------------------------------

plt.figtext(
    0.01,
    0.01,
    "Source: Our World in Data energy dataset",
    fontsize=8,
    color="gray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# ----------------------------------------
# 7. SAVE THE CHART
# ----------------------------------------

output_dir = project_dir / "outputs" / "figures"

output_dir.mkdir(
    parents=True,
    exist_ok=True
)

output_path = (
    output_dir / "global_electricity_mix.png"
)

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

print("\nChart saved successfully!")
print(output_path)

# ----------------------------------------
# 8. DISPLAY THE CHART
# ----------------------------------------

plt.show()
