# Book management system example demonstrating optional arguments and default values in dataclass

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    price: float = 0.0  # Default value for price
    genre: Optional[str] = None  # Optional field with default value None


# Creating book instances
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)
book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald")  # Using default price
book4 = Book(
    4, "Moby Dick", "Herman Melville", genre="Fiction"
)  # Using default price and setting genre

# Accessing and printing book details
print(f"Book 1: {book1}")
print(f"Book 2: {book2}")
print(f"Book 3: {book3}")
print(f"Book 4: {book4}")


# Creating a library class using dataclass with a default empty list for books
@dataclass
class Library:
    name: str
    books: List[Book] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Book {book.title} added to {self.name} library."


# Creating a library instance
library = Library("Central Library")

# Adding books to the library
print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))
print(library.add_book(book4))

# Printing the books in the library
print("\nBooks in Central Library:")
for book in library.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}, Genre: {book.genre}"
    )
