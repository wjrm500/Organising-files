import os
import shutil
import hashlib

source_dirs = [
    r"D:\Documents copied from laptop 02.04.2022",
    r"D:\Documents",
    r"D:\2019-11-17 File Deposit (Files no longer on live PC so do not delete this!)\Document snapshot (files still live)",
    r"D:\EVERY DOCUMENT copied from laptop 29.01.17",
    r"D:\EVERY DOCUMENT copied from laptop 12.01.17",
    r"D:\Documents copied from laptop 09.01.16",
    r"D:\Documents copied from laptop 11.05.16",
]

destination_dir = r"D:\Merged_Documents"

def md5_checksum(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        for byte_block in iter(lambda: file.read(4096), b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

def merge_directories(src_dirs, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    seen_files = {}

    for src_dir in src_dirs:
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_checksum = md5_checksum(file_path)
                rel_path = os.path.relpath(root, src_dir)
                dest_subdir = os.path.join(dest_dir, rel_path)

                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)

                dest_file_path = os.path.join(dest_subdir, file)

                if file_checksum not in seen_files.values():
                    if os.path.exists(dest_file_path):
                        i = 1
                        while True:
                            file_name, file_ext = os.path.splitext(file)
                            new_file_name = f"{file_name}_{i}{file_ext}"
                            dest_file_path = os.path.join(dest_subdir, new_file_name)
                            if not os.path.exists(dest_file_path):
                                break
                            i += 1

                    shutil.copy(file_path, dest_file_path)
                    seen_files[file_path] = file_checksum
                    print(f"Copied {file_path} to {dest_file_path}")

merge_directories(source_dirs, destination_dir)
