import os
import hashlib
import json

destination_dir = r"D:\Merged_Documents"

def md5_checksum(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        for byte_block in iter(lambda: file.read(4096), b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

def analyze_files(dest_dir):
    file_checksums = {}
    file_sizes = {}

    total_files = 0
    processed_files = 0

    for root, _, files in os.walk(dest_dir):
        total_files += len(files)

    for root, _, files in os.walk(dest_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_checksum = md5_checksum(file_path)
            file_size = os.path.getsize(file_path)

            if file_checksum not in file_checksums:
                file_checksums[file_checksum] = [file_path]
            else:
                file_checksums[file_checksum].append(file_path)

            file_sizes[file_path] = file_size

            processed_files += 1
            print(f"Processed {processed_files}/{total_files}: {file_path}")

    return file_checksums, file_sizes

def save_to_file(data, filename):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_directory, filename)

    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)

    print(f"Saved data to {output_path}")

def process_results(file_checksums, file_sizes):
    duplicates = {k: v for k, v in file_checksums.items() if len(v) > 1}
    sorted_file_sizes = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)

    print("\nDuplicate files:")
    for paths in duplicates.values():
        for path in paths:
            print(path)

    print("\nLargest files:")
    for path, size in sorted_file_sizes:
        print(f"{path} - {size} bytes")

    save_to_file(duplicates, 'duplicates.json')
    save_to_file(sorted_file_sizes, 'largest_files.json')

file_checksums, file_sizes = analyze_files(destination_dir)
process_results(file_checksums, file_sizes)
