# Explanation of StringIO in Python's io Module
# TIMESTAMP__2024_08_11__123421

from io import StringIO


# Function to demonstrate the use of StringIO
def stringio_example():
    # Create a StringIO object
    file_like_object = StringIO()

    # Write to the StringIO object
    file_like_object.write("This is a test.\n")
    file_like_object.write("StringIO allows us to treat strings as files.\n")

    # Reset the cursor to the beginning of the StringIO object
    file_like_object.seek(0)

    # Read from the StringIO object
    content = file_like_object.read()

    # Close the StringIO object
    file_like_object.close()

    return content


# Use the function and print the result
result = stringio_example()
print("Content of the StringIO object:")
print(result)
