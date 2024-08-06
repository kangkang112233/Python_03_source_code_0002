# Using copytree() and ignore_patterns() in Python
# TIMESTAMP__2024_08_04__152943
# This example demonstrates how to use copytree() and ignore_patterns() in a library management system.

import shutil
from shutil import ignore_patterns

# Define the source and destination directories
src_dir = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\test__"
dest_dir = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\test02"

# Copy the directory, ignoring specified patterns
shutil.copytree(src_dir, dest_dir, ignore=ignore_patterns("*.pyc", "tmp*"))

print(
    f"Copied {src_dir} to {dest_dir}, ignoring '*.pyc' files and 'tmp*' files/directories."
)
