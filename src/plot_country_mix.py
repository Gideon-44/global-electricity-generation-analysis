
import pandas as pd
import matplotlib.pyplot as plt

# Load country electricity mix results
df = pd.read_csv(
    "data/processed/country_electricity_mix_2025.csv"
)

# Sort countries by renewable share
df = df.sort_values(
    by="Renewables (%)",
    ascending=True
)

# Define chart categories
categories = [
    "Renewables (%)",
    "Fossil fuels (%)",
    "Nuclear (%)"
]

labels = [
    "Renewables",
    "Fossil fuels",
    "Nuclear"
]

colors = [
    "#2E8B57",
    "#D97706",
    "#4169A1"
]

# Create chart
fig, ax = plt.subplots(figsize=(11, 6))

left = [0] * len(df)

for category, label, color in zip(categories, labels, colors):
    values = df[category]

    ax.barh(
        df["Country"],
        values,
        left=left,
        label=label,
        color=color
    )

    # Add percentage labels to sufficiently large segments
    for i, value in enumerate(values):
        if value >= 5:
            ax.text(
                left[i] + value / 2,
                i,
                f"{value:.1f}%",
                ha="center",
                va="center",
                color="white",
                fontsize=9,
                fontweight="bold"
            )

    left = [
        left[i] + values.iloc[i]
        for i in range(len(df))
    ]

# Chart formatting
ax.set_title(
    "Electricity Generation Mix by Country — 2025",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Share of electricity generation (%)")
ax.set_ylabel("")

ax.set_xlim(0, 100)
ax.legend(
    title="Electricity source",
    loc="lower center",
    bbox_to_anchor=(0.5, -0.25),
    ncol=3,
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
    "outputs/figures/country_electricity_mix_2025.png",
    dpi=300,
    bbox_inches="tight"
)

print("Chart saved to:")
print("outputs/figures/country_electricity_mix_2025.png")

plt.show()