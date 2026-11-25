
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(
    "data/processed/cyp2c19_diplotype_phenotypes.csv"
)

phenotype_order = [
    "Poor metabolizer",
    "Intermediate metabolizer",
    "Normal metabolizer",
    "Rapid metabolizer",
    "Ultrarapid metabolizer"
]

print("CYP2C19 PHENOTYPE DATA")
print("----------------------")
print(df.to_string(index=False))

print("\nDATASET DIMENSIONS")
print("------------------")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nMISSING VALUES")
print("--------------")
print(df.isnull().sum())

phenotype_counts = (
    df["phenotype"]
    .value_counts()
    .reindex(phenotype_order, fill_value=0)
)

print("\nPHENOTYPE DISTRIBUTION")
print("----------------------")
print(phenotype_counts)

phenotype_percentages = (
    phenotype_counts / len(df) * 100
).round(2)

phenotype_summary = pd.DataFrame({
    "diplotype_count": phenotype_counts,
    "percentage": phenotype_percentages
})

print("\nPHENOTYPE SUMMARY")
print("-----------------")
print(phenotype_summary)

# Create output directory
os.makedirs("results", exist_ok=True)

# Plot phenotype distribution
fig, ax = plt.subplots(figsize=(10, 6))

phenotype_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "Distribution of CYP2C19 Metabolizer Phenotypes"
)

ax.set_xlabel("Metabolizer Phenotype")
ax.set_ylabel("Number of Reference Diplotypes")

ax.tick_params(
    axis="x",
    rotation=30
)

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_phenotype_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

activity_mapping = {
    "Poor metabolizer": "Reduced activity",
    "Intermediate metabolizer": "Reduced activity",
    "Normal metabolizer": "Normal activity",
    "Rapid metabolizer": "Increased activity",
    "Ultrarapid metabolizer": "Increased activity"
}

df["activity_group"] = df["phenotype"].map(
    activity_mapping
)

activity_counts = (
    df["activity_group"]
    .value_counts()
    .reindex(
        [
            "Reduced activity",
            "Normal activity",
            "Increased activity"
        ],
        fill_value=0
    )
)

print("\nDIPLOTYPE DISTRIBUTION BY FUNCTIONAL ACTIVITY")
print("---------------------------------------------")
print(activity_counts)

print("\nDIPLOTYPES BY ACTIVITY GROUP")
print("----------------------------")

for group in activity_counts.index:
    print(f"\n{group}:")

    print(
        df.loc[
            df["activity_group"] == group,
            "diplotype"
        ].tolist()
    )

fig, ax = plt.subplots(figsize=(9, 5))

activity_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title(
    "CYP2C19 Diplotype Distribution by Functional Activity"
)

ax.set_xlabel("Functional Activity Group")
ax.set_ylabel("Number of Reference Diplotypes")

ax.tick_params(
    axis="x",
    rotation=0
)

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_functional_activity_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
