# Book management system example using functools.wraps to preserve function metadata

import functools


# Decorator function to add logging and preserve function metadata
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")

        result = func(*args, **kwargs)

        print(f"Function {func.__name__} returned: {result}")
        return result

    return wrapper


# Function to add a book to the library
@log_decorator
def add_book(library, book):
    """Add a book to the library."""
    library.append(book)
    return f"Book {book['title']} added."


# Function to remove a book from the library
@log_decorator
def remove_book(library, book_id):
    """Remove a book from the library by its ID."""
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
print("\nFinal library state:")
for book in library:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")

# Verifying that metadata is preserved
print(f"\nFunction name: {add_book.__name__}")
print(f"Function docstring: {add_book.__doc__}")
