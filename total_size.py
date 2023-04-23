import os

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

def get_directory_size(dir_path):
    total_size = 0
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

def format_size(size_in_bytes):
    size_units = ["B", "KB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    size = float(size_in_bytes)

    while size >= 1024 and unit_index < len(size_units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.2f} {size_units[unit_index]}"

def print_directory_sizes(src_dirs, dest_dir):
    for src_dir in src_dirs:
        size = get_directory_size(src_dir)
        print(f"{src_dir}: {format_size(size)}")

    dest_size = get_directory_size(dest_dir)
    print(f"{dest_dir}: {format_size(dest_size)}")

print_directory_sizes(source_dirs, destination_dir)
