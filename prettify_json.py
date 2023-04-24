import json

with open('largest_files.json', 'r') as f:
    data = json.load(f)

pretty_data = json.dumps(data, indent=4)

with open('largest_files_pretty.json', 'w') as f:
    f.write(pretty_data)
