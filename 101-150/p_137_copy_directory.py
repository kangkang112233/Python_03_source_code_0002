# Using copytree() to Copy Directories in Python
# TIMESTAMP__2024_08_04__153512
# This example demonstrates how to use copytree() in a library management system.

import shutil
import os

# Define the source and destination directories
src_dir = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\test__"
dest_dir = "destination_directory"

# Ensure the destination directory does not exist
if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)

# Copy the directory
shutil.copytree(src_dir, dest_dir)

print(f"Copied {src_dir} to {dest_dir}")
