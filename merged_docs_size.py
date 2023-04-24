import os

def get_total_size(directory):
    total_size = 0
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

merged_documents_dir = r"D:\Merged_Documents"
total_size = get_total_size(merged_documents_dir)
print(f"Total size of Merged_Documents: {total_size} bytes")
