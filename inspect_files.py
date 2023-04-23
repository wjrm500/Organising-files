import os
import time
from datetime import datetime

start_time = time.time()

# Create a dictionary to store file paths, file sizes, and last modified times
file_dict = {}

# Iterate through all files in the directory
print("Scanning directory for files...")
for root, dirs, files in os.walk("D:/"):
    for file in files:
        file_path = os.path.join(root, file)
        mod_time = os.path.getmtime(file_path)
        size = os.path.getsize(file_path)
        print("Found file:", file_path)
        # Check if file name, size, and modified time already exist in the dictionary
        if (file, size, mod_time) in file_dict:
            file_dict[(file, size, mod_time)].append(file_path)
            print("Matching file found for file name, size, and modified time:", file)
            print("File path:", file_path)
            print("Size:", size, "bytes", "- Last modified:", datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S'))
        else:
            file_dict[(file, size, mod_time)] = [file_path]

# Iterate through the dictionary and print file paths, file sizes, and last modified times
print("Printing matching file paths, file sizes, and last modified times...")
count = 0
for (file, size, mod_time), path_list in file_dict.items():
    if len(path_list) > 1:
        print("Matching files found for file name, size, and modified time:", file, "- Size:", size, "bytes", "- Last modified:", datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S'))
        for path in path_list:
            print("File path:", path)
        print()

        count += 1

# Print total count of matching files found
print("Total count of matching files found:", count)

# Print total time taken for the script to run
end_time = time.time()
total_time = end_time - start_time
print("Total time taken:", total_time, "seconds")
