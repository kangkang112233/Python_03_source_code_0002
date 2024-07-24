# This code example demonstrates the usage of getcwd(), listdir(), removedirs(), and rename()
# in the context of a library management system.

import os


def display_current_directory():
    """
    Display the current working directory.

    Returns:
    str: The current working directory.
    """
    return os.getcwd()


def list_directory_contents(path="."):
    """
    List the contents of the specified directory.

    Args:
    path (str): The path of the directory to list contents of.

    Returns:
    list: A list of files and directories in the specified directory.
    """
    return os.listdir(path)


def remove_directory(path):
    """
    Remove the specified directory.

    Args:
    path (str): The path of the directory to remove.

    Returns:
    None
    """
    os.removedirs(path)


def rename_item(src, dst):
    """
    Rename a file or directory from src to dst.

    Args:
    src (str): The current name of the file or directory.
    dst (str): The new name of the file or directory.

    Returns:
    None
    """
    os.rename(src, dst)


# Test cases
current_directory = display_current_directory()
print(f"Current directory: {current_directory}")

directory_contents = list_directory_contents()
print("\nDirectory contents:")
for item in directory_contents:
    print(item)

# Note: The following operations can modify your file system.
# Be careful with the paths you use.

# Example: Removing a test directory (uncomment to use)
# remove_directory('test_directory')

# Example: Renaming a test file (uncomment to use)
# rename_item('old_name.txt', 'new_name.txt')
