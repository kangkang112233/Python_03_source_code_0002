# JSON Handling
# TIMESTAMP__2024_08_03__110504
# This example demonstrates the use of `loads` and `dumps` in a library management system.

import json

# Sample JSON data representing a book
book_json = '''
{
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2021,
    "copies": 5
}
'''

# Converting JSON string to Python dictionary
book_dict = json.loads(book_json)
print(type(book_dict))
print("Loaded JSON data as dictionary:\n", book_dict)

# Modifying the book data
book_dict["copies"] += 1

# Converting Python dictionary back to JSON string
book_json_updated = json.dumps(book_dict, indent=4)
print("\nUpdated JSON data:\n", book_json_updated)
