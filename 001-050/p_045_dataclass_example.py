# Book management system example demonstrating the use of dataclass

from dataclasses import dataclass


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    price: float


# Creating book instances
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Accessing and printing book details
print(
    f"Book 1: ID={book1.book_id}, Title={book1.title}, Author={book1.author}, Price={book1.price}"
)
print(
    f"Book 2: ID={book2.book_id}, Title={book2.title}, Author={book2.author}, Price={book2.price}"
)

# Comparing books
print(f"Are the books the same? {'Yes' if book1 == book2 else 'No'}")


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
