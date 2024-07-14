# Book management system example demonstrating the default __eq__ method in dataclass

from dataclasses import dataclass


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    price: float


# Creating book instances with the same and different values
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(1, "1984", "George Orwell", 19.99)
book3 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Accessing and printing book details
print(f"Book 1: {book1}")
print(f"Book 2: {book2}")
print(f"Book 3: {book3}")

# Comparing books
print(f"Are book1 and book2 the same? {'Yes' if book1 == book2 else 'No'}")
print(f"Are book1 and book3 the same? {'Yes' if book1 == book3 else 'No'}")


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
print(library.add_book(book3))

# Printing the books in the library
print("\nBooks in Central Library:")
for book in library.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )
