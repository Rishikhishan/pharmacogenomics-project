import pandas as pd

reference_data = pd.read_csv(
    "data/processed/cyp2c19_diplotype_phenotypes.csv"
)
allele_data = pd.read_csv(
    "data/processed/cyp2c19_allele_functions.csv"
)

PRIMARY_ALLELES = {"*1", "*2", "*3", "*17"}

known_alleles = set(allele_data["star_allele"])

if known_alleles != PRIMARY_ALLELES:
    raise ValueError(
        f"Unexpected allele reference. Found: {known_alleles}"
    )

phenotype_lookup = dict(
    zip(
        reference_data["diplotype"],
        reference_data["phenotype"]
    )
)

expected_diplotypes = {
    "*1/*1",
    "*1/*2",
    "*1/*3",
    "*1/*17",
    "*2/*2",
    "*2/*3",
    "*2/*17",
    "*3/*3",
    "*3/*17",
    "*17/*17"
}

if len(reference_data) != 10:
    raise ValueError(
        "Reference table must contain exactly 10 diplotypes."
    )
if set(reference_data["diplotype"]) != expected_diplotypes:
    raise ValueError(
        "Reference table does not contain the expected 10 diplotypes."
    )
if reference_data["diplotype"].duplicated().any():
    raise ValueError(
        "Duplicate diplotypes found in reference table."
    )

def classify_diplotype(diplotype):

    alleles = diplotype.strip().split("/")

    if len(alleles) != 2:
        return "Invalid diplotype"

    if any(allele not in known_alleles for allele in alleles):
        return "Unknown allele"

    standard_diplotype = "/".join(sorted(
        alleles,
        key=lambda allele: ["*1", "*2", "*3", "*17"].index(allele)
    ))

    if standard_diplotype in phenotype_lookup:
        return phenotype_lookup[standard_diplotype]

    return "Unclassified diplotype"


# Test diplotypes
test_diplotypes = [
    "*1/*1",
    "*1/*2",
    "*1/*3",
    "*1/*17",
    "*2/*2",
    "*2/*3",
    "*2/*17",
    "*3/*3",
    "*3/*17",
    "*17/*17",
    "*2/*1",
    "*17/*2",
    "*1",
    "*1/*2/*3",
    "*1/*9",
    "*5/*17"
]

print("DIPLOTYPE CLASSIFICATION")
print("------------------------")

for diplotype in test_diplotypes:
    print(
        f"{diplotype}: "
        f"{classify_diplotype(diplotype)}"
    )


# Validate all reference-table entries
print("\nREFERENCE TABLE VALIDATION")
print("--------------------------")

correct = 0
total = len(reference_data)

for _, row in reference_data.iterrows():

    diplotype = row["diplotype"]
    expected = row["phenotype"]

    predicted = classify_diplotype(diplotype)

    if predicted == expected:
        correct += 1

    print(
        f"{diplotype}: "
        f"Expected = {expected} | "
        f"Predicted = {predicted}"
    )
print(f"\nCorrect predictions: {correct}/{total}")

if total > 0:
    print(f"Agreement: {correct / total * 100:.2f}%")