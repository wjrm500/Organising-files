import os
import shutil
import hashlib
import json

source_dirs = [
    r"D:\2019-11-17 File Deposit (everything except docs)"
]

destination_dir = r"D:\Merged_Documents"

script_directory = os.path.dirname(os.path.abspath(__file__))
seen_files_path = os.path.join(script_directory, 'seen_files.json')

ignored_formats = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']

def md5_checksum(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        for byte_block in iter(lambda: file.read(4096), b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

def get_seen_files(dest_dir):
    seen_files = []
    for root, _, files in os.walk(dest_dir):
        for file in files:
            if not any(file.lower().endswith(ext) for ext in ignored_formats):
                file_path = os.path.join(root, file)
                file_checksum = md5_checksum(file_path)
                seen_files.append(file_checksum)
                print(f"Seen file: {file_path}, Checksum: {file_checksum}")
    return seen_files

def save_seen_files(seen_files, file_path):
    with open(file_path, 'w') as outfile:
        json.dump(seen_files, outfile)
    print(f"Saved seen_files to {file_path}\n")

def merge_directories(src_dirs, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    print("Populating seen_files list...")
    seen_files = get_seen_files(dest_dir)
    save_seen_files(seen_files, seen_files_path)
    print("Finished populating seen_files list.\n")

    for src_dir in src_dirs:
        print(f"Processing source directory: {src_dir}")
        for root, _, files in os.walk(src_dir):
            for file in files:
                if not any(file.lower().endswith(ext) for ext in ignored_formats):
                    file_path = os.path.join(root, file)
                    file_checksum = md5_checksum(file_path)
                    rel_path = os.path.relpath(root, src_dir)
                    dest_subdir = os.path.join(dest_dir, rel_path)

                    if not os.path.exists(dest_subdir):
                        os.makedirs(dest_subdir)

                    dest_file_path = os.path.join(dest_subdir, file)

                    if file_checksum not in seen_files:
                        if os.path.exists(dest_file_path):
                            dest_checksum = md5_checksum(dest_file_path)
                            if dest_checksum != file_checksum:
                                i = 1
                                while True:
                                    file_name, file_ext = os.path.splitext(file)
                                    new_file_name = f"{file_name}_{i}{file_ext}"
                                    dest_file_path = os.path.join(dest_subdir, new_file_name)
                                    if not os.path.exists(dest_file_path):
                                        break
                                    i += 1
                        shutil.copy(file_path, dest_file_path)
                        print(f"Copied {file_path} to {dest_file_path}")
                    else:
                        print(f"Skipped duplicate: {file_path}")

        print(f"Finished processing source directory: {src_dir}\n")

merge_directories(source_dirs, destination_dir)
