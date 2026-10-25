
from pathlib import Path
import pandas as pd

data_folder = Path("data/processed")
annotation_file = data_folder / "cyp2c19_clopidogrel.csv"
variant_file = data_folder / "cyp2c19_variants.csv"

annotations = pd.read_csv(annotation_file)
variants = pd.read_csv(variant_file)

annotations.columns = annotations.columns.str.strip()
variants.columns = variants.columns.str.strip()

print("=== CLINPGX ANNOTATIONS ===")
print(f"Number of rows: {len(annotations)}")
print(f"Number of columns: {len(annotations.columns)}")
print("\nMissing values per column:")
print(annotations.isna().sum())

print("\n=== CYP2C19 VARIANT DATA ===")
print(f"Number of rows: {len(variants)}")
print(f"Number of columns: {len(variants.columns)}")

required_columns = [
    "rsID",
    "star_allele",
    "allele_count",
    "allele_number",
    "allele_frequency",
    "south_asian_allele_count",
    "south_asian_allele_number",
    "south_asian_frequency",
]

missing_columns = [
    column for column in required_columns
    if column not in variants.columns
]

if missing_columns:
    print("Missing required columns:", missing_columns)
else:
    print("\n=== FREQUENCY CONSISTENCY CHECK ===")

    for _, row in variants.iterrows():
        print(f"\nVariant: {row['star_allele']} ({row['rsID']})")

        checks = [
            (
                "Total",
                row["allele_count"],
                row["allele_number"],
                row["allele_frequency"],
            ),
            (
                "South Asian",
                row["south_asian_allele_count"],
                row["south_asian_allele_number"],
                row["south_asian_frequency"],
            ),
        ]

        for label, count, number, frequency in checks:
            count = pd.to_numeric(count, errors="coerce")
            number = pd.to_numeric(number, errors="coerce")
            frequency = pd.to_numeric(frequency, errors="coerce")

            if pd.isna(count) or pd.isna(number) or pd.isna(frequency):
                print(f"{label}: Missing or non-numeric data")
                continue

            if number <= 0 or count < 0 or count > number:
                print(f"{label}: INVALID allele counts")
                continue

            calculated_frequency = count / number
            difference = abs(calculated_frequency - frequency)

            if difference <= 0.0001:
                print(
                    f"{label}: PASS "
                    f"(recorded={frequency:.6f}, "
                    f"calculated={calculated_frequency:.6f})"
                )
            else:
                print(
                    f"{label}: CHECK "
                    f"(recorded={frequency:.6f}, "
                    f"calculated={calculated_frequency:.6f})"
                )

    print("\n=== DUPLICATE CHECK ===")
    print("Duplicate rsIDs:", int(variants["rsID"].duplicated().sum()))

print("\nValidation finished.")
