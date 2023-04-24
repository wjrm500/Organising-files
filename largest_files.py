import json

largest_files_file = 'largest_files.json'

def read_largest_files(file_path):
    with open(file_path, 'r') as infile:
        largest_files = json.load(infile)
    return largest_files

def print_top_largest_files(largest_files, num_top=50):
    sorted_largest_files = sorted(largest_files, key=lambda x: x[1], reverse=True)
    top_largest_files = sorted_largest_files[:num_top]

    print(f"Top {num_top} largest files:")
    for index, (file_path, file_size) in enumerate(top_largest_files, start=1):
        print(f"{index}. {file_path}")
        print(f"   File size: {file_size} bytes")

largest_files = read_largest_files(largest_files_file)
print_top_largest_files(largest_files, 250)
