import json
from datetime import datetime


# Custom class for books
class Book:
    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date


# Example book object
book = Book("Python Programming", "John Doe", datetime(2021, 5, 17))

# Serializing the book object to JSON without handling the custom object
try:
    book_json = json.dumps(book)
except TypeError as e:
    print(f"Error: {e}")
