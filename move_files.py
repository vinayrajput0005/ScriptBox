import os
import shutil

# Define the source directory where your files are located
source_directory = '/data/SRA_2021/fastp_Data'

# Define the destination directory where you want to copy the files
destination_directory = '/data/SRA_2021/February_2021/'

# Unique IDs to search for (without extensions)
unique_ids_to_find = [
   
"ERR7426597",
   # Add more unique IDs here
]

# Create a set to store the unique IDs found in the source directory
found_ids = set()

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    # Remove the file extension to get the base filename
    base_filename, file_extension = os.path.splitext(filename)
    
    # Check if the base filename (without extension) is in the list of unique IDs
    if base_filename in unique_ids_to_find:
        source_file = os.path.join(source_directory, filename)
        destination_file = os.path.join(destination_directory, filename)

        # Move the file to the destination directory
        shutil.move(source_file, destination_file)
        print(f"Moved {filename} to {destination_directory}")


        # Add the found ID to the set
        found_ids.add(base_filename)

# Check for missing unique IDs
missing_ids = set(unique_ids_to_find) - found_ids

if missing_ids:
    print("The following unique IDs were not found in the source directory:")
    for missing_id in missing_ids:
        print(missing_id)

print("Done copying files.")
