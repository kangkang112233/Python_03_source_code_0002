# Explanation of Path.glob() Method in Python
# TIMESTAMP__2024_08_12__124455

from pathlib import Path


# Function to demonstrate Path.glob() method
def demonstrate_path_glob(directory, pattern):
    path = Path(directory)
    search_result = path.glob(pattern)
    change_to_list = list(search_result)
    return change_to_list


# Example usage
directory = "."  # Current directory
pattern = "*.py"  # Pattern to match text files

# Finding files matching the pattern
matched_files = demonstrate_path_glob(directory, pattern)

print("Files matching the pattern:")
for file in matched_files:
    print(file)
