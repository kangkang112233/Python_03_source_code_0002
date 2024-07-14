# Book management system example demonstrating the problem and error with mutable default values in dataclass

from dataclasses import dataclass, field
from typing import List


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    price: float


try:

    @dataclass
    class Library:
        name: str
        books: List[Book] = []  # This will raise a ValueError

        def add_book(self, book: Book):
            self.books.append(book)
            return f"Book {book.title} added to {self.name} library."

    # Creating library instances
    library1 = Library("Central Library")
    library2 = Library("East Branch Library")

    # Adding books to libraries
    print(library1.add_book(Book(1, "1984", "George Orwell", 19.99)))
    print(library2.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)))

except ValueError as e:
    print(f"Error: {e}")


# Correcting the error by using field(default_factory=list)
@dataclass
class SafeLibrary:
    name: str
    books: List[Book] = field(default_factory=list)  # Correct way to set a default list

    def add_book(self, book: Book):
        self.books.append(book)
        return f"Book {book.title} added to {self.name} library."


# Creating library instances with correct implementation
safe_library1 = SafeLibrary("Central SafeLibrary")
safe_library2 = SafeLibrary("East Branch SafeLibrary")

# Adding books to libraries
print(safe_library1.add_book(Book(1, "1984", "George Orwell", 19.99)))
print(safe_library2.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)))

# Printing the books in each library
print("\nBooks in Central SafeLibrary:")
for book in safe_library1.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )

print("\nBooks in East Branch SafeLibrary:")
for book in safe_library2.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )
