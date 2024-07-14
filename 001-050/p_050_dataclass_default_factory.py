# Book management system example demonstrating the use of field(default_factory=list) in dataclass

from dataclasses import dataclass, field
from typing import List


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    price: float


@dataclass
class Library:
    name: str
    books: List[Book] = field(
        default_factory=list
    )  # Using default_factory to ensure each instance has its own list

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Book {book.title} added to {self.name} library."


# Creating book instances
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Creating library instances
library1 = Library("Central Library")
library2 = Library("East Branch Library")

# Adding books to libraries
print(library1.add_book(book1))
print(library1.add_book(book2))

print(library2.add_book(book1))

# Printing the books in each library
print("\nBooks in Central Library:")
for book in library1.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )

print("\nBooks in East Branch Library:")
for book in library2.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )
