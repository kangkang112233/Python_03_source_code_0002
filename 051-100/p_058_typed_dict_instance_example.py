# Book management system example demonstrating the direct instantiation of TypedDict

from typing import TypedDict, List


# Defining a TypedDict for Book
class BookDict(TypedDict):
    book_id: int
    title: str
    author: str
    price: float


# Creating book instances directly
book1: BookDict = {
    "book_id": 1,
    "title": "1984",
    "author": "George Orwell",
    "price": 19.99,
}
book2: BookDict = {
    "book_id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "price": 9.99,
}

# Printing book details
print("Book 1:", book1)
print("Book 2:", book2)


# Defining a TypedDict for Library
class LibraryDict(TypedDict):
    name: str
    books: List[BookDict]


# Creating a library instance directly
library: LibraryDict = {"name": "Central Library", "books": [book1, book2]}

# Printing library details
print("\nLibrary:", library)

# Accessing library books
print("\nBooks in the library:")
for book in library["books"]:
    print(
        f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}"
    )
