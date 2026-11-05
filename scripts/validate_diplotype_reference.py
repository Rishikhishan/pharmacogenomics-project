import pandas as pd

reference = pd.read_csv(
    "data/processed/cyp2c19_diplotype_phenotypes.csv"
)
alleles = pd.read_csv(
    "data/processed/cyp2c19_allele_functions.csv"
)
print("CYP2C19 Diplotype Reference Validation")
print("\n")
print(f"Number of diplotypes: {len(reference)}")

duplicates = reference["diplotype"].duplicated().sum()
print(f"Duplicate diplotypes: {duplicates}")

supported_alleles = set(alleles["star_allele"])
used_alleles = set(reference["allele_1"]) | set(reference["allele_2"])
unsupported = used_alleles - supported_alleles
print(f"Unsupported alleles: {unsupported}")

missing_phenotypes = reference["phenotype"].isna().sum()
missing_sources = reference["source"].isna().sum()
print(f"Missing phenotypes: {missing_phenotypes}")
print(f"Missing sources: {missing_sources}")

expected_diplotypes = (
    reference["allele_1"] + "/" + reference["allele_2"]
)
incorrect_diplotypes = (
    reference["diplotype"] != expected_diplotypes
).sum()

print(f"Incorrect diplotype labels: {incorrect_diplotypes}")
print("\nValidation complete.")
