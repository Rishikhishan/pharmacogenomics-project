
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(
    "data/processed/cyp2c19_allele_functions.csv"
)

print("CYP2C19 FUNCTIONAL CLASSIFICATION DATA")
print("--------------------------------------")
print(df.to_string(index=False))

print("\nDATASET DIMENSIONS")
print("------------------")
print(df.shape)

print("\nMISSING VALUES")
print("--------------")
print(df.isnull().sum())

category_counts = (
    df.groupby("function_category")["star_allele"]
    .count()
    .sort_values(ascending=False)
)

print("\nSTAR ALLELE DISTRIBUTION BY FUNCTION")
print("------------------------------------")
print(category_counts)

os.makedirs("results", exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 5))

category_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Distribution of CYP2C19 Star Alleles by Function"
)

ax.set_xlabel("Functional Category")
ax.set_ylabel("Number of Star Alleles")

ax.tick_params(axis="x", rotation=0)

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_functional_category_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

df_sorted = df.sort_values("star_allele")

ax.barh(
    df_sorted["star_allele"],
    [1] * len(df_sorted)
)

ax.set_title(
    "Functional Classification of CYP2C19 Star Alleles"
)

ax.set_xlabel("Star Allele (one entry per reference allele)")
ax.set_ylabel("CYP2C19 Star Allele")

ax.set_xticks([])

for i, row in enumerate(
    df_sorted.itertuples(index=False)
):
    ax.text(
        0.5,
        i,
        row.function,
        ha="center",
        va="center"
    )

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_star_allele_functional_mapping.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
