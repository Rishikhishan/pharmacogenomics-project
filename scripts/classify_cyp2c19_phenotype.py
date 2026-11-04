
import pandas as pd

allele_data = pd.read_csv(
    "data/processed/cyp2c19_allele_functions.csv"
)

allele_functions = dict(
    zip(
        allele_data["star_allele"],
        allele_data["function_category"]
    )
)

phenotype_rules = {
    ("normal", "normal"): "Normal metabolizer",

    ("increased", "normal"): "Rapid metabolizer",
    ("increased", "increased"): "Ultrarapid metabolizer",

    ("no_function", "normal"): "Intermediate metabolizer",
    ("increased", "no_function"): "Intermediate metabolizer",
    ("no_function", "no_function"): "Poor metabolizer"
}


def classify_diplotype(diplotype):
    alleles = diplotype.split("/")
    if len(alleles) != 2:
        return "Invalid diplotype"
    if any(allele not in allele_functions for allele in alleles):
        return "Unknown allele"
    categories = tuple(
        sorted(
            [allele_functions[allele] for allele in alleles]
        )
    )
    return phenotype_rules.get(
        categories,
        "Unclassified diplotype"
    )

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
    "*5/*17"
]

for diplotype in test_diplotypes:
    print(
        f"{diplotype}: "
        f"{classify_diplotype(diplotype)}"
    )
