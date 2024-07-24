import json


# Function to demonstrate JSON encoding in a library management system
def encode_book_info(book_info):
    """
    Encode book information to JSON format.
    """
    encoded_json = json.dumps(book_info, ensure_ascii=False, indent=4)
    return encoded_json


# Example usage
book_info = {
    "title": "Python Programming",
    "author": "John Doe",
    "published_year": 2020,
    "genres": ["Programming", "Technology"],
}

# Encode the book information to JSON format
encoded_book_info = encode_book_info(book_info)
print(f"Encoded book info:\n{encoded_book_info}")
print(type(encoded_book_info))
