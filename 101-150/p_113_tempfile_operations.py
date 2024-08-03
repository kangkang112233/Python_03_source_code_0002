# Knowledge Point: TemporaryFile(), NamedTemporaryFile(), TemporaryDirectory()

from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory


# Function to demonstrate the use of TemporaryFile
def use_temporary_file():
    with TemporaryFile(mode="w+t") as temp_file:
        temp_file.write("This is a temporary file without a name.")
        temp_file.seek(0)
        print("TemporaryFile content:")
        print(temp_file.read())


# Function to demonstrate the use of NamedTemporaryFile
def use_named_temporary_file():
    with NamedTemporaryFile(mode="w+t", delete=False) as named_temp_file:
        print(f"NamedTemporaryFile created: {named_temp_file.name}")
        named_temp_file.write("This is a temporary file with a name.")
        named_temp_file.seek(0)
        print("NamedTemporaryFile content:")
        print(named_temp_file.read())


# Function to demonstrate the use of TemporaryDirectory
def use_temporary_directory():
    with TemporaryDirectory() as temp_dir:
        print(f"TemporaryDirectory created: {temp_dir}")
        # You can create temporary files within this directory
        with open(f"{temp_dir}/tempfile.txt", "w+t") as temp_file:
            temp_file.write("This is a temporary file inside a temporary directory.")
            temp_file.seek(0)
            print("TemporaryDirectory content:")
            print(temp_file.read())


# Example usage in a library management system
print("Using TemporaryFile:")
use_temporary_file()

print("\nUsing NamedTemporaryFile:")
use_named_temporary_file()

print("\nUsing TemporaryDirectory:")
use_temporary_directory()
