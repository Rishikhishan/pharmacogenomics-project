import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(
    "data/processed/cyp2c19_variants.csv"
)

print("CYP2C19 VARIANT DATA")
print("--------------------")
print(df)

print("\nDATASET DIMENSIONS")
print("------------------")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nCOLUMN NAMES")
print("------------")
print(df.columns.tolist())

print("\nDATA TYPES")
print("----------")
print(df.dtypes)

print("\nMISSING VALUES")
print("--------------")
print(df.isnull().sum())

print("\nDESCRIPTIVE STATISTICS")
print("----------------------")
print(df.describe())


df["global_frequency_percent"] = (
    df["allele_frequency"] * 100
)

df["south_asian_frequency_percent"] = (
    df["south_asian_frequency"] * 100
)

df["frequency_difference"] = (
    df["south_asian_frequency_percent"]
    - df["global_frequency_percent"]
)

frequency_summary = df[
    [
        "star_allele",
        "rsID",
        "global_frequency_percent",
        "south_asian_frequency_percent",
        "frequency_difference",
        "south_asian_allele_count",
        "south_asian_allele_number"
    ]
].copy()

frequency_summary = frequency_summary.round(3)

print("\nSOUTH ASIAN CYP2C19 FREQUENCY SUMMARY")
print("-------------------------------------")

print(frequency_summary.to_string(index=False))

alleles = frequency_summary["star_allele"]

frequencies = (
    frequency_summary["south_asian_frequency_percent"]
)

plt.figure(figsize=(8, 5))

plt.bar(alleles, frequencies)

plt.title("CYP2C19 Variant Allele Frequencies in South Asians")
plt.xlabel("CYP2C19 Star Allele")
plt.ylabel("Allele Frequency (%)")

plt.ylim(0, 36)

for index, value in enumerate(frequencies):
    plt.text(
        index,
        value + 0.5,
        f"{value:.2f}%",
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    "results/cyp2c19_south_asian_frequencies.png",
    dpi=300
)

plt.show()
