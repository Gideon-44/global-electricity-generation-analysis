
import pandas as pd
import matplotlib.pyplot as plt

# Load country growth results
df = pd.read_csv(
    "data/processed/country_electricity_growth_2000_2025.csv"
)

# Sort by absolute generation increase
df = df.sort_values(
    by="Increase (TWh)",
    ascending=True
)

# Create chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    df["country"],
    df["Increase (TWh)"]
)

# Add value labels
for bar in bars:
    width = bar.get_width()

    if width >= 0:
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" +{width:,.1f} TWh",
            va="center",
            ha="left",
            fontsize=9
        )
    else:
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {width:,.1f} TWh",
            va="center",
            ha="right",
            fontsize=9
        )

# Chart formatting
ax.axvline(0, linewidth=0.8)

ax.set_title(
    "Change in Electricity Generation by Country (2000–2025)",
    fontsize=13,
    fontweight="bold"
)

ax.set_xlabel("Change in electricity generation (TWh)")
ax.set_ylabel("")

ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

ax.set_axisbelow(True)

plt.tight_layout()

# Save chart
plt.savefig(
    "outputs/figures/country_generation_growth_2000_2025.png",
    dpi=300,
    bbox_inches="tight"
)

print("Chart saved to:")
print("outputs/figures/country_generation_growth_2000_2025.png")

plt.show()
