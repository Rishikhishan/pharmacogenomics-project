import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(
    "data/processed/cyp2c19_variants.csv"
)

df["global_percent"] = (
    df["allele_frequency"] * 100
)

df["south_asian_percent"] = (
    df["south_asian_frequency"] * 100
)

df = df.sort_values("south_asian_percent")

fig, ax = plt.subplots(figsize=(9, 5))

y_positions = range(len(df))

for y, (_, row) in zip(y_positions, df.iterrows()):

    ax.plot(
        [row["global_percent"],
         row["south_asian_percent"]],
        [y, y],
        color="gray",
        linewidth=2,
        zorder=1
    )

ax.scatter(
    df["global_percent"],
    y_positions,
    label="Global",
    marker="o",
    s=90,
    zorder=2
)

ax.scatter(
    df["south_asian_percent"],
    y_positions,
    label="South Asian",
    marker="D",
    s=90,
    zorder=3
)

ax.set_yticks(list(y_positions))
ax.set_yticklabels(df["star_allele"])

ax.set_title(
    "Global vs South Asian CYP2C19 Allele Frequencies"
)

ax.set_xlabel("Allele Frequency (%)")
ax.set_ylabel("CYP2C19 Star Allele")

ax.legend(title="Population")

ax.grid(axis="x", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_global_vs_south_asian.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()