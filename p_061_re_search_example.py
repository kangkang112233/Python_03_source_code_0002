# Book management system example demonstrating the use of re.search

import re


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title_pattern):
        for index, book in enumerate(self.books):
            if re.search(title_pattern, book.title):
                return index, re.search(title_pattern, book.title)
        return -1, None


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book[ID: {self.book_id}, Title: {self.title}, Author: {self.author}]"


# Creating book instances
book1 = Book(1, "1984", "George Orwell")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald")

# Creating a library instance and adding books to it
library = Library("Central Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Searching for books by title pattern
index, match = library.find_book(r"1984")
print("Searching for '1984':", index, match.group() if match else "Not found")

index, match = library.find_book(r"Mockingbird")
print("Searching for 'Mockingbird':", index, match.group() if match else "Not found")

index, match = library.find_book(r"Moby Dick")
print("Searching for 'Moby Dick':", index, match.group() if match else "Not found")

# Printing book details
print("\nBooks in the library:")
for book in library.books:
    print(book)
