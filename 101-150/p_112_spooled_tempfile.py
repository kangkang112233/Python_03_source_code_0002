# Knowledge Point: SpooledTemporaryFile()

from tempfile import SpooledTemporaryFile


# Function to demonstrate the use of SpooledTemporaryFile
def manage_large_data():
    # Create a spooled temporary file with a maximum size of 100 bytes in memory
    with SpooledTemporaryFile(max_size=100, mode="w+") as temp_file:
        # Write some data to the temporary file
        temp_file.write(
            "This is a test string that will be stored in memory until it exceeds 100 bytes."
        )

        # Seek to the beginning and read the data
        temp_file.seek(0)
        print("Data in memory:")
        print(temp_file.read())

        # Write more data to exceed the memory limit
        temp_file.write(
            " Adding more data to exceed the in-memory limit and spool to disk."
        )

        # Check if the file has been spooled to disk
        if temp_file._rolled:
            print("\nData has been spooled to disk.")
        else:
            print("\nData is still in memory.")

        # Seek to the beginning and read the data again
        temp_file.seek(0)
        print("\nData after exceeding memory limit:")
        content = temp_file.read()
        print(content)

        # Return the content read from the temporary file
        return content


# Example usage in a library management system
file_content = manage_large_data()

# Output the content
print("\nFinal content read from the temporary file:")
print(file_content)
