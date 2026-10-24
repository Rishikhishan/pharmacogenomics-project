print("Script started")
from pathlib import Path
import pandas as pd

file_path = Path("data/raw/clopidogrel-annotations.csv")
if not file_path.exists():
    raise FileNotFoundError(f"File not found:{file_path}")
df = pd.read_csv(file_path)
print("\n ---Datasets dimensions---")
print(f"Rows:{df.shape[0]}")
print(f"Columns:{df.shape[1]}")
print("\n---Column names---")
print(df.columns.tolist())
print("\n---First 5 rows---")
print(df.head().to_string(index=False))
print("\n---Data types---")
print(df.dtypes.to_string())
print("\n---Missing values---")
print(df.isna().sum().to_string())