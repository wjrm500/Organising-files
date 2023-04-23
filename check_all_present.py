import json
import os
import hashlib

source_dirs = [
    # r"D:\Documents copied from laptop 02.04.2022",
    # r"D:\Documents",
    # r"D:\2019-11-17 File Deposit (docs)",
    r"D:\2019-11-17 File Deposit (everything except docs)",
    r"D:\EVERY DOCUMENT copied from laptop 29.01.17",
    # r"D:\EVERY DOCUMENT copied from laptop 12.01.17",
    # r"D:\Documents copied from laptop 09.01.16",
    # r"D:\Documents copied from laptop 11.05.16",
]

destination_dir = r"D:\Merged_Documents"

script_directory = os.path.dirname(os.path.abspath(__file__))

def md5_checksum(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        for byte_block in iter(lambda: file.read(4096), b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

def get_file_checksums(dir_path):
    file_checksums = {}
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_checksum = md5_checksum(file_path)
            file_checksums[file_path] = file_checksum
    return file_checksums

def save_dest_checksums(dest_checksums):
    dest_checksums_path = os.path.join(script_directory, 'dest_checksums.json')
    with open(dest_checksums_path, 'w') as outfile:
        json.dump(dest_checksums, outfile)
    print(f"Saved dest_checksums to {dest_checksums_path}")

def load_dest_checksums():
    dest_checksums_path = os.path.join(script_directory, 'dest_checksums.json')
    if os.path.exists(dest_checksums_path):
        with open(dest_checksums_path, 'r') as infile:
            dest_checksums = json.load(infile)
        print(f"Loaded dest_checksums from {dest_checksums_path}")
        return dest_checksums
    else:
        print(f"No dest_checksums available at {dest_checksums_path}")
        return None

def ensure_all_files_present(src_dirs, dest_dir):
    dest_checksums = load_dest_checksums()
    if dest_checksums is None:
        dest_checksums = get_file_checksums(dest_dir)
        save_dest_checksums(dest_checksums)

    missing_files = []

    file_count = {}

    for src_dir in src_dirs:
        print(f"Checking for missing files from '{src_dir}'...")
        src_checksums = get_file_checksums(src_dir)
        file_count[src_dir] = {"present": 0, "missing": 0}  # create keys if not present
        for file_path, file_checksum in src_checksums.items():
            if file_checksum not in dest_checksums.values():
                missing_files.append(file_path)
                file_count[src_dir]["missing"] += 1
            else:
                file_count[src_dir]["present"] += 1

    if missing_files:
        print("The following files are missing in the Merged_Documents directory:")
        for file_path in missing_files:
            print(file_path)
    else:
        print("All files are present in the Merged_Documents directory.")
    
    print(file_count)

    # Write missing_files to file
    missing_files_path = os.path.join(script_directory, 'missing_files.txt')
    with open(missing_files_path, 'w') as outfile:
        outfile.write('\n'.join(missing_files))
    print(f"Saved missing_files to {missing_files_path}")

    # Write file_count to file
    file_count_path = os.path.join(script_directory, 'file_count.json')
    with open(file_count_path, 'w') as outfile:
        json.dump(file_count, outfile)
    print(f"Saved file_count to {file_count_path}")

ensure_all_files_present(source_dirs, destination_dir)