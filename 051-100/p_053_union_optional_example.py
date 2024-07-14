# Book management system example demonstrating the use of Union and Optional in type hints

from typing import Union, Optional


class Book:
    def __init__(
        self, book_id: int, title: str, author: str, price: Optional[float] = None
    ):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def set_price(self, price: Union[float, None]):
        self.price = price

    def __str__(self):
        return f"Book[ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Price: {self.price}]"


# Creating book instances
book1 = Book(1, "1984", "George Orwell")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Setting the price using set_price method
book1.set_price(19.99)
book2.set_price(None)  # Setting price to None

# Printing book details
print(book1)
print(book2)


# Function to find a book by title, demonstrating the use of Optional in return type
def find_book_by_title(books: list[Book], title: str) -> Optional[Book]:
    for book in books:
        if book.title == title:
            return book
    return None


# List of books
library_books = [book1, book2]

# Finding a book by title
found_book = find_book_by_title(library_books, "1984")
print(f"\nFound book: {found_book}")

# Attempting to find a book that doesn't exist
missing_book = find_book_by_title(library_books, "Nonexistent Book")
print(f"Found book: {missing_book}")
