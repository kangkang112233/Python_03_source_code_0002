# Book management system example using a retry decorator

import time
import random


# Decorator function to retry a function upon failure
def retry_decorator(retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)  # Try to execute the function
                except Exception as e:  # If an exception occurs
                    attempt += 1  # Increment the attempt counter
                    print(f"Attempt {attempt} failed: {e}")
                    time.sleep(delay)  # Wait for a specified delay before retrying
            raise Exception(
                f"Function {func.__name__} failed after {retries} attempts"
            )  # Raise an exception if all retries fail

        return wrapper

    return decorator


# Sample function to simulate database connection
@retry_decorator(retries=3, delay=2)
def connect_to_database():
    if random.choice([True, False]):  # Randomly simulate a connection failure
        raise ConnectionError("Failed to connect to the database.")
    return "Connected to the database."


# Function to add a book to the library with a simulated unreliable database connection
@retry_decorator(retries=3, delay=2)
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
