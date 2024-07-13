# Book management system example using retrying for retry decorator

from retrying import retry
import random


# Retry decorator using retrying library
@retry(stop_max_attempt_number=3, wait_fixed=2000)
def connect_to_database():
    if random.choice([True, False]):
        raise ConnectionError("Failed to connect to the database.")
    return "Connected to the database."


# Function to add a book to the library with a simulated unreliable database connection
@retry(stop_max_attempt_number=3, wait_fixed=2000)
def add_book_to_library(library, book):
    connection_status = connect_to_database()
    print(connection_status)
    library.append(book)
    return f"Book {book['title']} added to the library."


# Sample book library
library = []

# Adding books to the library
try:
    add_book_to_library(
        library, {"id": 1, "title": "Book Title 1", "author": "Author A"}
    )
    add_book_to_library(
        library, {"id": 2, "title": "Book Title 2", "author": "Author B"}
    )
except Exception as e:
    print(e)

# Printing the final state of the library
print("\nFinal library state:")
for book in library:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
