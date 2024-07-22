# This script demonstrates how to specify the return type of a function.
# Application context: Managing a library system with books

from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


def get_books_published_after(year: int, books: List[Book]) -> List[Book]:
    """
    Returns a list of books published after the specified year.

    :param year: The year to filter books by.
    :param books: The list of books to filter.
    :return: A list of books published after the specified year.
    """
    return [book for book in books if book.year > year]


# Creating a list of books
books = [
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("Brave New World", "Aldous Huxley", 1932),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
]

# Getting books published after 1950
books_after_1950 = get_books_published_after(1950, books)

print("Books published after 1950:")
for book in books_after_1950:
    print(f"- {book.display_info()}")
