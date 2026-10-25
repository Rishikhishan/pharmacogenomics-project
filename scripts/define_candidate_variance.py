
import pandas as pd
from pathlib import Path

candidate_variants = [
    {
        "star_allele": "*2",
        "rsID": "rs4244285",
        "function": "No function",
        "frequency_verified": False,
    },
    {
        "star_allele": "*3",
        "rsID": "rs4986893",
        "function": "No function",
        "frequency_verified": False,
    },
    {
        "star_allele": "*17",
        "rsID": "rs12248560",
        "function": "Increased function",
        "frequency_verified": False,
    },
]

df = pd.DataFrame(candidate_variants)

output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "candidate_variants.csv"
df.to_csv(output_file, index=False)

print(df.to_string(index=False))
print(f"\nSaved to: {output_file}")
