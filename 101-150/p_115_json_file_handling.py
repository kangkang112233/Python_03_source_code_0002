# Knowledge Point: JSON Module - load() and dump() functions

import json


# Function to save book data to a JSON file
def save_books_to_json(file_path, books):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


# Function to load book data from a JSON file
def load_books_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Example usage in a library management system
books = [
    {"title": "Book A", "author": "Author 1", "year": 2021},
    {"title": "Book B", "author": "Author 2", "year": 2020},
    {"title": "Book C", "author": "Author 3", "year": 2019},
]

# Save books to a JSON file
save_books_to_json("books.json", books)
print("Books data has been written to 'books.json'.")

# Load books from the JSON file
loaded_books = load_books_from_json("books.json")
print("\nLoaded books data:")
print(loaded_books)
