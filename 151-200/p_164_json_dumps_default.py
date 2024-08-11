import json


# Custom class for books
class Book:
    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date


# Function to convert Book objects to a dictionary
def book_to_dict(obj):
    if isinstance(obj, Book):
        return {
            "title": obj.title,
            "author": obj.author,
            "published_date": obj.published_date.strftime("%Y-%m-%d"),
        }
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


# Another custom class
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year


# Example of a non-Book object
author = Author("John Doe", 1980)

# Attempting to serialize the Author object to JSON with book_to_dict function
try:
    author_json = json.dumps(author, default=book_to_dict)
except TypeError as e:
    print(f"Error: {e}")
