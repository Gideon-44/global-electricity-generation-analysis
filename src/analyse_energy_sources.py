
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

world = world.sort_values("year")

# ----------------------------------------
# 3. DEFINE ELECTRICITY SOURCES
# ----------------------------------------

major_sources = {
    "coal_electricity_twh": "Coal",
    "gas_electricity_twh": "Gas",
    "hydro_electricity_twh": "Hydro",
    "oil_electricity_twh": "Oil",
    "nuclear_electricity_twh": "Nuclear",
}

emerging_sources = {
    "solar_electricity_twh": "Solar",
    "wind_electricity_twh": "Wind",
    "bioenergy_electricity_twh": "Bioenergy",
}

# ----------------------------------------
# 4. DISPLAY LATEST AVAILABLE VALUES
# ----------------------------------------

print("\nGLOBAL ELECTRICITY GENERATION BY SOURCE")
print("---------------------------------------")

all_sources = {
    **major_sources,
    **emerging_sources,
}

for column, name in all_sources.items():

    available = world.dropna(subset=[column])

    if available.empty:
        print(f"{name}: No available observations")
        continue

    latest = available.iloc[-1]

    print(
        f"{name}: "
        f"{latest['year']} | "
        f"{latest[column]:,.2f} TWh"
    )

# ----------------------------------------
# 5. CREATE A REUSABLE CHART FUNCTION
# ----------------------------------------

def create_source_chart(source_dictionary, title, filename):

    plt.figure(figsize=(12, 6))

    for column, name in source_dictionary.items():

        plt.plot(
            world["year"],
            world[column],
            label=name,
            linewidth=2
        )

    plt.title(title, fontsize=16)

    plt.xlabel("Year", fontsize=12)

    plt.ylabel(
        "Electricity Generation (TWh)",
        fontsize=12
    )

    plt.legend()

    plt.grid(True, alpha=0.3)

    plt.figtext(
        0.01,
        0.01,
        "Source: Our World in Data energy dataset",
        fontsize=8,
        color="gray"
    )

    plt.tight_layout(rect=[0, 0.04, 1, 1])

    output_dir = project_dir / "outputs" / "figures"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = output_dir / filename

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"\nChart saved: {output_path}")

    plt.show()

# ----------------------------------------
# 6. CHART 1: MAJOR ELECTRICITY SOURCES
# ----------------------------------------

create_source_chart(
    major_sources,
    "Global Electricity Generation by Major Source",
    "major_electricity_sources.png"
)

# ----------------------------------------
# 7. CHART 2: SOLAR, WIND AND BIOENERGY
# ----------------------------------------

create_source_chart(
    emerging_sources,
    "Global Electricity Generation: Solar, Wind and Bioenergy",
    "emerging_electricity_sources.png"
)

print("\nENERGY SOURCE ANALYSIS COMPLETED!")
