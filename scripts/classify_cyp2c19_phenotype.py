
import pandas as pd

reference_data = pd.read_csv(
    "data/processed/cyp2c19_diplotype_phenotypes.csv"
)

allele_data = pd.read_csv(
    "data/processed/cyp2c19_allele_functions.csv"
)
known_alleles = set(allele_data["star_allele"])

phenotype_lookup = dict(
    zip(
        reference_data["diplotype"],
        reference_data["phenotype"]
    )
)

phenotype_rules = {
    ("normal", "normal"): "Normal metabolizer",
    ("increased", "normal"): "Rapid metabolizer",
    ("increased", "increased"): "Ultrarapid metabolizer",
    ("no_function", "normal"): "Intermediate metabolizer",
    ("increased", "no_function"): "Intermediate metabolizer",
    ("no_function", "no_function"): "Poor metabolizer",
    ("decreased", "normal"): "Likely intermediate metabolizer",
    ("decreased", "increased"): "Likely intermediate metabolizer",
    ("decreased", "decreased"): "Likely intermediate metabolizer",
    ("decreased", "no_function"): "Likely poor metabolizer"
}


def classify_diplotype(diplotype):
    alleles = diplotype.split("/")

    if len(alleles) != 2:
        return "Invalid diplotype"

    if any(allele not in known_alleles for allele in alleles):
        return "Unknown allele"

    if diplotype in phenotype_lookup:
        return phenotype_lookup[diplotype]

    reversed_diplotype = "/".join(reversed(alleles))

    if reversed_diplotype in phenotype_lookup:
        return phenotype_lookup[reversed_diplotype]

    return "Unclassified diplotype"

test_diplotypes = [
    "*1/*1",
    "*1/*2",
    "*2/*17",
    "*2/*2",
    "*1/*17",
    "*17/*17",
    "*2/*1",
    "*17/*2",
    "*1",
    "*1/*2/*3",
    "*1/*9",
    "*5/*17",
    "*1/*9",
    "*9/*17",
    "*9/*9",
    "*2/*9",
    "*3/*9"
]

for diplotype in test_diplotypes:
    print(
        f"{diplotype}: "
        f"{classify_diplotype(diplotype)}"
    )

print("\nReference Table Validation")
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
print(f"Accuracy: {correct / total * 100:.2f}%")