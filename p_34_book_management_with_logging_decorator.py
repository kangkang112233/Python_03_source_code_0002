# Book management system example using decorator for logging

# Importing required modules
import functools


# Decorator function to add logging
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}\n")
        return result

    return wrapper


# Function to add a book to the library
@log_decorator
def add_book(library, book):
    library.append(book)
    return f"Book {book['title']} added."


# Function to remove a book from the library
@log_decorator
def remove_book(library, book_id):
    for book in library:
        if book["id"] == book_id:
            library.remove(book)
            return f"Book {book['title']} removed."
    return "Book not found."


# Sample book library
library = []

# Adding books to the library
add_book(library, {"id": 1, "title": "Book Title 1", "author": "Author A"})
add_book(library, {"id": 2, "title": "Book Title 2", "author": "Author B"})

# Removing a book from the library
remove_book(library, 1)

# Trying to remove a non-existent book
remove_book(library, 3)

# Printing the final state of the library
print("Final library state:")
for book in library:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
