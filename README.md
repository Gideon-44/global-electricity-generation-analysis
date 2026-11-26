# Global Electricity Generation: Trends, Sources and Country Comparisons

## Project Overview

This project analyses global electricity generation using data from Our World in Data (OWID).

The analysis explores how electricity generation has changed over time, the contribution of different energy sources, and how electricity generation and energy mixes compare across selected countries.

The project uses Python for data cleaning, validation, analysis and visualisation.

## Project Objectives

- Analyse long-term trends in global electricity generation.
- Compare fossil fuel and low-carbon electricity generation.
- Examine the contribution of individual electricity sources.
- Compare electricity generation across China, the United States, India, Germany and Kenya.
- Analyse changes in national electricity generation and energy mixes between 2000 and 2025.
- Apply data quality checks to improve the reliability of the analysis.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git and GitHub

## Data Source

**Source:** Our World in Data (OWID), Energy dataset.

**Dataset:** [OWID Energy Dataset](https://catalog.ourworldindata.org/garden/energy/2026-09-10/owid_energy/owid_energy.csv)

The dataset contains electricity generation information for countries and regional aggregates across multiple years.

Generation values are measured in terawatt-hours (TWh).

## Project Structure

```text
project-1-electricity-generation/
│
├── data/
│   ├── raw/
│   │   └── owid_energy.csv
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── tests/
│
├── outputs/
│   └── figures/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Methodology

### 1. Data Inspection

Inspected the original dataset to understand its structure, available variables, year coverage, missing values and duplicate records.

### 2. Data Cleaning

- Selected relevant electricity generation variables.
- Retained standard three-letter ISO-coded entities and the World aggregate.
- Checked for duplicate entity-year records.
- Reviewed missing and negative generation values.
- Saved the cleaned dataset for analysis.

Missing values were not automatically treated as zero.

### 3. Data Quality Testing

Created automated tests to check:

- Required columns.
- Valid entity names and years.
- ISO code formatting.
- Duplicate entity-year records.
- Negative generation values.
- Missing electricity generation values.
- Electricity mix percentage consistency.

All eight data quality tests passed during the project validation.

### 4. Analysis and Visualisation

Used Python and Matplotlib to examine global electricity generation, energy sources, country-level generation, growth and changes in electricity mix.

## Key Findings

### Global Electricity Generation

- Global electricity generation increased from approximately **6.36 TWh in 1900** to **31,772.35 TWh in 2025**.
- This demonstrates substantial long-term growth in electricity production.

### Global Electricity Mix in 2025

- Fossil fuels accounted for approximately **57.39%** of global electricity generation.
- Low-carbon sources accounted for approximately **42.61%**.

Low-carbon electricity includes renewable sources and nuclear power.

### Electricity Sources

In 2025:

- Coal remained the largest individual electricity source, contributing approximately **32.96%** of global generation.
- Solar and wind together contributed approximately **17.29%**.
- Gas generation increased substantially between 2000 and 2025.
- Oil-fired electricity generation declined over the same period.

### Country Comparisons

The analysis of five selected countries found that:

- China had the highest electricity generation among the five countries in 2025, at approximately 10,583.36 TWh.
- The United States generated approximately 4,519.79 TWh.
- India generated approximately 2,081.60 TWh.
- Germany generated approximately 500.47 TWh.
- Kenya generated approximately 14.04 TWh.

### Changes in Renewable Electricity Share

Between 2000 and 2025, the renewable share of electricity generation increased in all five selected countries:

- Germany: approximately 52.87 percentage-point increase.
- Kenya: approximately 49.66 percentage-point increase.
- China: approximately 20.40 percentage-point increase.
- United States: approximately 16.41 percentage-point increase.
- India: approximately 10.02 percentage-point increase.

These are changes in electricity mix percentages, not changes in absolute electricity generation.

## Outputs

The project produces analytical datasets and visualisations, including:

- Global electricity generation trend.
- Global fossil fuel and low-carbon electricity mix.
- Major and emerging electricity source trends.
- Country electricity generation comparisons.
- Country electricity mix comparisons.
- Country generation growth comparisons.
- Changes in renewable electricity shares.

Figures are saved in `outputs/figures/`, while processed datasets are saved in `data/processed/`.

## Data Quality and Limitations

- Electricity generation data availability varies by country and year.
- Historical values may be estimated or revised.
- Missing values should not be interpreted as zero generation.
- The country comparison focuses on five selected countries and is not a complete global country ranking.
- Electricity mix percentages describe the relative contribution of sources, not their absolute generation.
- The analysis is descriptive and does not establish causal relationships.

## Reproducibility

The project uses Python and the packages listed in `requirements.txt`.

To reproduce the analysis:

1. Clone or download the repository.
2. Create and activate a Python virtual environment.
3. Install the required packages.
4. Ensure the raw OWID dataset is available in `data/raw/`.
5. Run the data cleaning and analysis scripts in `src/`.
6. Run the automated tests using:

```bash
python -m pytest -v
```

## Future Improvements

- Develop an automated data download process.
- Expand the country comparison to include more countries.
- Build an interactive dashboard.
- Explore electricity generation trends alongside energy demand and emissions.
- Add further statistical analysis of changes in electricity generation.

## Author

Energy Data Analysis Portfolio Project

