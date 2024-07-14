# Book management system example demonstrating the use of frozen dataclass

from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    book_id: int
    title: str
    author: str
    price: float


# Creating book instances
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Accessing and printing book details
print(f"Book 1: {book1}")
print(f"Book 2: {book2}")

# Attempting to modify an attribute will raise a FrozenInstanceError
try:
    book1.price = 21.99
except AttributeError as e:
    print(f"Error: {e}")


# Creating a library class using dataclass
@dataclass
class Library:
    name: str
    books: list

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Book {book.title} added to {self.name} library."


# Creating a library instance
library = Library("Central Library", [])

# Adding books to the library
print(library.add_book(book1))
print(library.add_book(book2))

# Printing the books in the library
print("\nBooks in Central Library:")
for book in library.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )
