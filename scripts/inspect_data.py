from pathlib import Path
raw_folder = Path("data/raw")
if not raw_folder.exists():
    raise FileNotFoundError("Could not find the data/raw folder")
files = sorted(raw_folder.iterdir())
print("files found in data/raw:")
for file in files:
    if file.is_file():
        size_kb = file.stat().st_size / 1024
        print(f"{file.name} - {size_kb:.1f} KB")