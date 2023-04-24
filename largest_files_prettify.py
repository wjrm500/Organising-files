import json
import os

with open('largest_files.json', 'r') as f:
    data = json.load(f)

with open('largest_files.txt', 'w', encoding='utf-8') as f:
    for item in data:
        filepath = item[0]
        file_size = item[1]

        # Format file size as human readable
        size_suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
        size_idx = 0
        while file_size >= 1024 and size_idx < len(size_suffixes) - 1:
            file_size /= 1024
            size_idx += 1
        human_readable_size = f"{file_size:.2f} {size_suffixes[size_idx]}"

        # Write file size and filepath to text file
        f.write(f"{human_readable_size} - {filepath}\n")
