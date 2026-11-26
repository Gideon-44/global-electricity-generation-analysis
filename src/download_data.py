
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

    temp_file = OUTPUT_DIR / "owid_energy.tmp"

    print("Starting dataset download...")

    try:
        with requests.get(
            DATA_URL,
            stream=True,
            timeout=(15, 120)
        ) as response:
            response.raise_for_status()

            with temp_file.open("wb") as file:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        file.write(chunk)

        # Replace the existing dataset only after a successful download
        temp_file.replace(OUTPUT_FILE)

        file_size_mb = OUTPUT_FILE.stat().st_size / (1024 * 1024)

        print("Download successful!")
        print(f"Saved to: {OUTPUT_FILE}")
        print(f"File size: {file_size_mb:.2f} MB")

    except requests.RequestException as error:
        temp_file.unlink(missing_ok=True)
        print(f"Download failed: {error}")
        raise

    except OSError:
        temp_file.unlink(missing_ok=True)
        raise

if __name__ == "__main__":
    download_dataset()