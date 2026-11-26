
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load country electricity mix changes
df = pd.read_csv(
    "data/processed/country_electricity_mix_change.csv"
)

# Separate 2000 and 2025 data
data_2000 = df[df["year"] == 2000].copy()
data_2025 = df[df["year"] == 2025].copy()

# Sort countries by renewable share in 2025
data_2025 = data_2025.sort_values(
    by="Renewables (%)",
    ascending=True
)

countries = data_2025["country"].tolist()

# Match the same country order in both datasets
data_2000 = data_2000.set_index("country").loc[countries]
data_2025 = data_2025.set_index("country").loc[countries]

y = np.arange(len(countries))
height = 0.35

# Create chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    y - height / 2,
    data_2000["Renewables (%)"],
    height,
    label="2000"
)

ax.barh(
    y + height / 2,
    data_2025["Renewables (%)"],
    height,
    label="2025"
)

# Add chart labels
ax.set_yticks(y)
ax.set_yticklabels(countries)

ax.set_xlabel("Renewable share of electricity generation (%)")

ax.set_title(
    "Change in Renewable Electricity Share: 2000 vs 2025",
    fontsize=13,
    fontweight="bold"
)

ax.set_xlim(0, 100)

ax.legend(
    title="Year",
    frameon=False
)

ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

ax.set_axisbelow(True)

plt.tight_layout()

# Save chart
plt.savefig(
    "outputs/figures/country_renewable_share_change.png",
    dpi=300,
    bbox_inches="tight"
)

print("Chart saved to:")
print("outputs/figures/country_renewable_share_change.png")

plt.show()
