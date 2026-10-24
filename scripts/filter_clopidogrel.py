from pathlib import Path
import pandas as pd 
input_file = Path("data/raw/clopidogrel-annotations.csv")
output_folder = Path("data/processed")
output_file = output_folder / "cyp2c19_clopidogrel.csv"
df = pd.read_csv(input_file)
df.columns = df.columns.str.strip()
filtered_df = df[
    (df["Gene"] == "CYP2C19") &
    (df["Drugs"].str.lower() == "clopidogrel")
].copy()
output_folder.mkdir(parents=True, exist_ok=True)
filtered_df.to_csv(output_file, index=False)
print(f"Oringinal rows: {len(df)}")
print(f"matching rows: {len(filtered_df)}")
print(f"Saved to: {output_file}")
print("\nSelected annotations:")
print(filtered_df.to_string(index=False))
