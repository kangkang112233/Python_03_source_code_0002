# Temporary Files in Python
# TIMESTAMP__2024_08_04__152058
# This example demonstrates the use of NamedTemporaryFile in a library management system.

import tempfile
import os


def create_temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file_name = temp_file.name

    # Check if the temporary file exists
    file_exists = os.path.exists(temp_file_name)
    print(f"Temporary file exists: {file_exists}")

    # Read the content of the temporary file
    with open(temp_file_name, "r") as file:
        content = file.read()
        print(f"Content of temporary file: {content}")

    # Clean up the temporary file
    os.remove(temp_file_name)
    print(f"Temporary file exists after cleanup: {os.path.exists(temp_file_name)}")


if __name__ == "__main__":
    create_temp_file()
