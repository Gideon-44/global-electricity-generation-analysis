

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
# 2. SELECT GLOBAL ELECTRICITY GENERATION
# ----------------------------------------

world = df[df["country"] == "World"].copy()

world = world.dropna(
    subset=["electricity_generation_twh"]
)

world = world.sort_values("year")

# ----------------------------------------
# 3. PRINT KEY FINDINGS
# ----------------------------------------

print("\nGLOBAL ELECTRICITY GENERATION")
print("-----------------------------")

print("First year:", world["year"].min())
print("Latest year:", world["year"].max())

print(
    "First reported generation (TWh):",
    round(world.iloc[0]["electricity_generation_twh"], 2)
)

print(
    "Latest reported generation (TWh):",
    round(world.iloc[-1]["electricity_generation_twh"], 2)
)

print("\nMost recent 10 observations:")

print(
    world[["year", "electricity_generation_twh"]]
    .tail(10)
    .to_string(index=False)
)

# ----------------------------------------
# 4. CREATE THE VISUALISATION
# ----------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    world["year"],
    world["electricity_generation_twh"],
    linewidth=2
)

plt.title(
    "Global Electricity Generation (1900–2025)",
    fontsize=16
)

plt.xlabel("Year", fontsize=12)
plt.ylabel("Electricity Generation (TWh)", fontsize=12)

plt.grid(True, alpha=0.3)

plt.figtext(
    0.01,
    0.01,
    "Source: Our World in Data energy dataset | "
    "Electricity generation measured in TWh",
    fontsize=8,
    color="gray"
)

plt.tight_layout(rect=[0, 0.04, 1, 1])

# ----------------------------------------
# 5. SAVE THE CHART
# ----------------------------------------

output_dir = project_dir / "outputs" / "figures"
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "global_electricity_generation.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

print("\nChart saved to:")
print(output_path)

plt.show()
