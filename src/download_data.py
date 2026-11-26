
from pathlib import Path
import requests

# Dataset source: Our World in Data
DATA_URL = (
    "https://catalog.ourworldindata.org/garden/"
    "energy/2026-09-10/owid_energy/owid_energy.csv"
)

# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Where the original dataset will be stored
OUTPUT_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_FILE = OUTPUT_DIR / "owid_energy.csv"

def download_dataset():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Starting dataset download...")

    response = requests.get(DATA_URL, timeout=120)
    response.raise_for_status()

    OUTPUT_FILE.write_bytes(response.content)

    file_size_mb = OUTPUT_FILE.stat().st_size / (1024 * 1024)

    print("Download successful!")
    print(f"Saved to: {OUTPUT_FILE}")
    print(f"File size: {file_size_mb:.2f} MB")


if __name__ == "__main__":
    download_dataset()
