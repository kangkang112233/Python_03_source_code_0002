# Explanation of dumps method with default parameter in Python
# TIMESTAMP__2024_08_11__150834

import json
from datetime import datetime


# Custom class for books
class Book:
    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date


# Function to convert Book objects to a dictionary
def book_to_dict(book):
    if isinstance(book, Book):
        return {
            "title": book.title,
            "author": book.author,
            "published_date": book.published_date.strftime("%Y-%m-%d"),
        }
    raise TypeError(
        f"Object of type {book.__class__.__name__} is not JSON serializable"
    )


# Example book object
book = Book("Python Programming", "John Doe", datetime(2021, 5, 17))

# Serializing the book object to JSON
book_json = json.dumps(book, default=book_to_dict, indent=4)

print("Serialized book object to JSON:")
print(book_json)
