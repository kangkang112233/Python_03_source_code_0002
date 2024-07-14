# Book management system example demonstrating the use of TypedDict

from typing import TypedDict, List


# Defining a TypedDict for Book
class BookDict(TypedDict):
    book_id: int
    title: str
    author: str
    price: float


# Function to create a book
def create_book(book_id: int, title: str, author: str, price: float) -> BookDict:
    return BookDict(book_id=book_id, title=title, author=author, price=price)


# Creating book instances
book1 = create_book(1, "1984", "George Orwell", 19.99)
book2 = create_book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Printing book details
print("Book 1:", book1)
print("Book 2:", book2)


# Defining a TypedDict for Library
class LibraryDict(TypedDict):
    name: str
    books: List[BookDict]


# Function to create a library
def create_library(name: str, books: List[BookDict]) -> LibraryDict:
    return LibraryDict(name=name, books=books)


# Creating a library instance
library = create_library("Central Library", [book1, book2])

# Printing library details
print("\nLibrary:", library)

# Accessing library books
print("\nBooks in the library:")
for book in library["books"]:
    print(
        f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}"
    )
