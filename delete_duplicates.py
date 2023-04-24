import json
import os

with open('duplicates.json', 'r') as f:
    data = json.load(f)

for checksum, filepaths in data.items():
    if len(filepaths) > 1:
        print(f"Deleting duplicates for checksum {checksum}")
        for filepath in filepaths[1:]:
            if os.path.isfile(filepath):
                os.remove(filepath)
                print(f"Deleted file: {filepath}")
            else:
                print(f"File not found: {filepath}")
