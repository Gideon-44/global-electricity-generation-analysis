
import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]

raw_path = project_dir / "data" / "raw" / "owid_energy.csv"
clean_path = project_dir / "data" / "processed" / "electricity_generation_clean.csv"

for label, path in [
    ("RAW DATA", raw_path),
    ("CLEANED DATA", clean_path),
]:
    df = pd.read_csv(path)

    # Find rows whose country name is exactly World
    world = df[
        df["country"].astype(str).str.strip().str.casefold() == "world"
    ]

    print(f"\n{label}")
    print("-" * 35)
    print("World records found:", len(world))

    if not world.empty:
        columns = [
            col for col in [
                "country",
                "year",
                "iso_code",
                "electricity_generation_twh",
            ]
            if col in world.columns
        ]

        print(world[columns].head(10).to_string(index=False))
