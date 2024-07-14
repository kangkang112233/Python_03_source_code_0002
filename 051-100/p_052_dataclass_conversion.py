# Book management system example demonstrating the use of asdict and astuple for dataclass conversion

from dataclasses import dataclass, asdict, astuple
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
    books: List[Book]

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Book {book.title} added to {self.name} library."

    def to_dict(self):
        return asdict(self)

    def to_tuple(self):
        return astuple(self)


# Creating book instances
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Creating a library instance
library = Library("Central Library", [])

# Adding books to the library
print(library.add_book(book1))
print(library.add_book(book2))

# Converting the library to a dictionary
library_dict = library.to_dict()
print("\nLibrary as dictionary:")
print(library_dict)

# Converting the library to a tuple
library_tuple = library.to_tuple()
print("\nLibrary as tuple:")
print(library_tuple)

# Printing the books in the library
print("\nBooks in Central Library:")
for book in library.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )
