# This code example demonstrates the usage of Path.cwd(), Path.exists(), Path.touch(), and Path.unlink()
# in the context of a library management system.

from pathlib import Path


def library_directory_operations():
    """
    Perform directory operations for the library system.

    Returns:
    None
    """
    # Get the current directory
    current_directory = Path.cwd()
    print(f"Current directory: {current_directory}")

    # Define a new file path
    new_file = current_directory / "new_book_list.txt"

    # Check if the file exists
    if not new_file.exists():
        # Create the file
        new_file.touch()
        print(f"Created file: {new_file}")
    else:
        print(f"File already exists: {new_file}")

    # Remove the file
    if new_file.exists():
        new_file.unlink()
        print(f"Deleted file: {new_file}")


# Run the function
library_directory_operations()
