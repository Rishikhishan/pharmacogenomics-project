
import pandas as pd
from pathlib import Path

variant_data = {
    "rsID": "rs4244285",
    "variant_id": "10-94781859-G-A",
    "gene": "CYP2C19",
    "star_allele": "*2",
    "assembly": "GRCh38",
    "dataset": "gnomAD v4.1.2",
    "allele_count": 234686,
    "allele_number": 1464646,
    "allele_frequency": 0.1602,
    "south_asian_frequency": 0.3203,
    "frequency_warning": (
        "Exome/genome frequencies flagged as discrepant"
    ),
}

df = pd.DataFrame([variant_data])

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "cyp2c19_variants.csv"
df.to_csv(output_file, index=False)

print(df.to_string(index=False))
print(f"\nSaved to: {output_file}")
