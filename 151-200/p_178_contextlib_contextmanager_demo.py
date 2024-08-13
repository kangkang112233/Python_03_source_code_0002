# Explanation of contextlib.contextmanager in Python
# TIMESTAMP__2024_08_12__162315

import contextlib


# Example function demonstrating contextlib.contextmanager
@contextlib.contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()


# Usage example
def main():
    file_path = "example.txt"
    with open_file(file_path, "w") as f:
        f.write("Hello, World!")
    print(f"File '{file_path}' written successfully.")


if __name__ == "__main__":
    main()
