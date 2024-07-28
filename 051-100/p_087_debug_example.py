import pdb


# Example for a library management system
# Simulating a function to add a book to the library
def add_book_to_library(title, author):
    book = {"title": title, "author": author}
    # Inserting a breakpoint to debug the function
    breakpoint()
    return book


# Another function to find a book in the library
def find_book_in_library(title, library):
    for book in library:
        if book["title"] == title:
            # Using pdb.set_trace() for debugging
            pdb.set_trace()
            return book
    return None


# Simulating library data
library = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "Brave New World", "author": "Aldous Huxley"},
]

# Adding a new book
new_book = add_book_to_library("Fahrenheit 451", "Ray Bradbury")
library.append(new_book)

# Finding a book
found_book = find_book_in_library("1984", library)
print(f"Found Book: {found_book}")

# Output:
# Found Book: {'title': '1984', 'author': 'George Orwell'}
