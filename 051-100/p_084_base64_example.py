import base64


# Function to demonstrate Base64 encoding and decoding in a library management system
def encode_book_cover(image_path):
    """
    Encode the book cover image to Base64.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def decode_book_cover(encoded_string, output_path):
    """
    Decode the Base64 string back to an image.
    """
    image_data = base64.b64decode(encoded_string)
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)


# Example usage
input_image = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\panda.jpg"
encoded_image_string = encode_book_cover(input_image)
print(
    f"Encoded image string:\n{encoded_image_string[:100]}..."
)  # Display first 100 characters for brevity

output_image = "decoded_panda.jpg"
decode_book_cover(encoded_image_string, output_image)
print(f"Image has been decoded and saved to {output_image}")
