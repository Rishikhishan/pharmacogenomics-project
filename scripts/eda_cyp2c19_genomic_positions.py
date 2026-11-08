
import pandas as pd
import matplotlib.pyplot as plt
import os
from itertools import combinations

df = pd.read_csv(
    "data/processed/cyp2c19_variants.csv"
)

df["chromosome"] = (
    df["variant_id"].str.split("-").str[0]
)

df["position"] = pd.to_numeric(
    df["variant_id"].str.split("-").str[1]
)

print("REFERENCE ASSEMBLY")
print("------------------")
print(df["assembly"].value_counts())

print("\nCHROMOSOME DISTRIBUTION")
print("-----------------------")
print(df["chromosome"].value_counts())

df = df.sort_values("position")

position_summary = df[
    [
        "star_allele",
        "rsID",
        "chromosome",
        "position",
        "function",
        "assembly"
    ]
]

print("\nCYP2C19 GENOMIC POSITION SUMMARY")
print("--------------------------------")
print(position_summary.to_string(index=False))

df["position_mb"] = df["position"] / 1_000_000

os.makedirs("results", exist_ok=True)

fig, ax = plt.subplots(figsize=(11, 5))

y_positions = [0] * len(df)

ax.hlines(
    y=0,
    xmin=df["position_mb"].min() - 0.002,
    xmax=df["position_mb"].max() + 0.002,
    color="gray",
    linewidth=2
)

ax.scatter(
    df["position_mb"],
    y_positions,
    s=120,
    zorder=3
)

for i, (_, row) in enumerate(df.iterrows()):

    offset = 35 if i % 2 == 0 else -55

    ax.annotate(
        f'{row["star_allele"]}\n'
        f'{row["rsID"]}\n'
        f'{row["position"]:,}',
        xy=(row["position_mb"], 0),
        xytext=(0, offset),
        textcoords="offset points",
        ha="center",
        fontsize=9,
        arrowprops=dict(
            arrowstyle="-",
            color="gray"
        )
    )

ax.set_title(
    "Genomic Distribution of Selected CYP2C19 Variants"
)

ax.set_xlabel(
    "Genomic Position on Chromosome 10 (Mb, GRCh38)"
)

ax.set_ylabel("")

ax.set_yticks([])

ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_genomic_positions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGENOMIC DISTANCES")
print("-----------------")

for (_, variant1), (_, variant2) in combinations(
    df.iterrows(), 2
):

    distance = abs(
        variant2["position"] - variant1["position"]
    )

    print(
        f'{variant1["star_allele"]} to '
        f'{variant2["star_allele"]}: '
        f'{distance:,} bp'
    )

