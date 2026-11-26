
import pandas as pd
import matplotlib.pyplot as plt

# Load country growth results
df = pd.read_csv(
    "data/processed/country_electricity_growth_2000_2025.csv"
)

# Sort by percentage growth
df = df.sort_values(
    by="Growth (%)",
    ascending=True
)

# Create chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    df["country"],
    df["Growth (%)"]
)

# Add percentage labels
for bar in bars:
    width = bar.get_width()

    if width >= 0:
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" +{width:.1f}%",
            va="center",
            ha="left",
            fontsize=9
        )
    else:
        ax.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {width:.1f}%",
            va="center",
            ha="right",
            fontsize=9
        )

# Chart formatting
ax.axvline(0, linewidth=0.8)

ax.set_title(
    "Percentage Growth in Electricity Generation (2000–2025)",
    fontsize=13,
    fontweight="bold"
)

ax.set_xlabel("Percentage change (%)")
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
    "outputs/figures/country_percentage_growth_2000_2025.png",
    dpi=300,
    bbox_inches="tight"
)

print("Chart saved to:")
print("outputs/figures/country_percentage_growth_2000_2025.png")

plt.show()
