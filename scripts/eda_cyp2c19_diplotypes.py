
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(
    "data/processed/cyp2c19_diplotype_phenotypes.csv"
)

print("CYP2C19 DIPLOTYPE DATA")
print("----------------------")
print(df.to_string(index=False))

print("\nDATASET DIMENSIONS")
print("------------------")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nCOLUMN NAMES")
print("------------")
print(df.columns.tolist())

print("\nMISSING VALUES")
print("--------------")
print(df.isnull().sum())

print("\nPHENOTYPE DISTRIBUTION")
print("----------------------")
print(df["phenotype"].value_counts())

phenotype_counts = (
    df["phenotype"]
    .value_counts()
)

print("\nDIPLOTYPE COMBINATIONS BY PHENOTYPE")
print("----------------------------------")
print(phenotype_counts)

os.makedirs("results", exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 6))

phenotype_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Distribution of CYP2C19 Diplotype Combinations by Phenotype"
)

ax.set_xlabel("Metabolizer Phenotype")
ax.set_ylabel("Number of Diplotype Combinations")

ax.tick_params(
    axis="x",
    rotation=30
)

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_diplotype_phenotype_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

df_sorted = df.sort_values(
    ["phenotype", "diplotype"]
)

fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(
    df_sorted["diplotype"],
    [1] * len(df_sorted)
)

ax.set_title(
    "CYP2C19 Diplotype-to-Phenotype Mapping"
)

ax.set_xlabel(
    "Reference diplotype (one entry per combination)"
)

ax.set_ylabel("CYP2C19 Diplotype")

ax.set_xticks([])

for i, row in enumerate(
    df_sorted.itertuples(index=False)
):
    ax.text(
        0.5,
        i,
        row.phenotype,
        ha="center",
        va="center"
    )

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_diplotype_phenotype_mapping.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
