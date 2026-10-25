
import pandas as pd
from pathlib import Path

variant_data = [
    {
        "rsID": "rs4244285",
        "variant_id": "10-94781859-G-A",
        "gene": "CYP2C19",
        "star_allele": "*2",
        "function": "No function",
        "assembly": "GRCh38",
        "dataset": "gnomAD v4.1.2",
        "allele_count": 234686,
        "allele_number": 1464646,
        "allele_frequency": 0.1602,
        "south_asian_allele_count": 20947,
        "south_asian_allele_number": 65396,
        "south_asian_frequency": 0.3203,
        "frequency_warning": "Exome/genome frequencies flagged as discrepant",
    },
    {
        "rsID": "rs4986893",
        "variant_id": "10-94780653-G-A",
        "gene": "CYP2C19",
        "star_allele": "*3",
        "function": "No function",
        "assembly": "GRCh38",
        "dataset": "gnomAD v4.1.2",
        "allele_count": 4750,
        "allele_number": 1613588,
        "allele_frequency": 0.002944,
        "south_asian_allele_count": 317,
        "south_asian_allele_number": 91064,
        "south_asian_frequency": 0.003481,
        "frequency_warning": "Exome/genome frequencies flagged as discrepant",
    },
    {
        "rsID": "rs12248560",
        "variant_id": "10-94761900-C-T",
        "gene": "CYP2C19",
        "star_allele": "*17",
        "function": "Increased function",
        "assembly": "GRCh38",
        "dataset": "gnomAD v4.1.2",
        "allele_count": 30385,
        "allele_number": 151940,
        "allele_frequency": 0.2000,
        "south_asian_allele_count": 785,
        "south_asian_allele_number": 4820,
        "south_asian_frequency": 0.1629,
        "frequency_warning": "Not in exomes; genome data only",
    },
]

df = pd.DataFrame(variant_data)

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "cyp2c19_variants.csv"
df.to_csv(output_file, index=False)

print(df.to_string(index=False))
print(f"\nSaved to: {output_file}")
