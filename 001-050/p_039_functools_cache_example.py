# Book management system example using functools.lru_cache for caching

import functools


# Sample function to simulate fetching book details from a database
@functools.lru_cache(maxsize=128)
def fetch_book_details(book_id):
    print(f"Fetching details for book ID: {book_id}")
    # Simulate a database fetch with a delay
    import time

    time.sleep(2)
    return {
        "id": book_id,
        "title": f"Book Title {book_id}",
        "author": f"Author {book_id}",
    }


# Function to add a book to the library
def add_book(library, book_id):
    book_details = fetch_book_details(book_id)
    library.append(book_details)
    return f"Book {book_details['title']} added to the library."


# Sample book library
library = []

# Adding books to the library
print(add_book(library, 1))
print(add_book(library, 2))

# Fetching the same book again to demonstrate caching
print(add_book(library, 1))

# Printing the final state of the library
print("\nFinal library state:")
for book in library:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
