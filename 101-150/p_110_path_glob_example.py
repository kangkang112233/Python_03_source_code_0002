# Knowledge Point: Path.glob() method

from pathlib import Path


# Function to list all .txt files in the given directory
def list_txt_files(directory):
    path = Path(directory)
    txt_files = path.glob("*.txt")

    print(type(txt_files))

    # Print each .txt file found
    for txt_file in txt_files:
        print(f"Found .txt file: {txt_file}")


# Example usage in a library management system
list_txt_files(
    "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002"
)

# This will output all .txt files in the specified directory
