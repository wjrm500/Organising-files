import os

def get_directory_sizes(directory):
    directory_sizes = {}
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            total_size = 0
            for dirpath, _, filenames in os.walk(dir_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            directory_sizes[dir_path] = total_size
            print(f"Processed directory: {dir_path}, Size: {total_size} bytes")
    return directory_sizes

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def save_directory_sizes(directory_sizes, file_path):
    sorted_directory_sizes = sorted(directory_sizes.items(), key=lambda x: x[1], reverse=True)
    with open(file_path, "w", encoding='utf-8') as outfile:
        for dir_path, size in sorted_directory_sizes:
            size_human_readable = convert_size(size)
            outfile.write(f"{size_human_readable}\t{dir_path}\n")
    print(f"Saved directory sizes to {file_path}")

merged_documents_dir = r"D:\Merged_Documents"
output_file = r"largest_directories.txt"

import math
directory_sizes = get_directory_sizes(merged_documents_dir)
save_directory_sizes(directory_sizes, output_file)
