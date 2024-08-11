# Explanation of Type Hints for Collections
# TIMESTAMP__2024_08_11__112241

from typing import List, Dict


# Function to add a new book to the library with type hints
def add_book(
    library: List[Dict[str, str]], book: Dict[str, str]
) -> List[Dict[str, str]]:
    library.append(book)
    return library


# Example library list with type hints
library: List[Dict[str, str]] = [
    {"title": "Python Programming", "author": "John Doe"},
    {"title": "Data Science with Python", "author": "Jane Smith"},
]

# New book to add
new_book: Dict[str, str] = {"title": "Machine Learning Basics", "author": "Alan Turing"}

# Adding the new book to the library
updated_library = add_book(library, new_book)

# Printing the updated library
print("Updated Library:")
for book in updated_library:
    print(f"Title: {book['title']}, Author: {book['author']}")
