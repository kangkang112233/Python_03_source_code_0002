# __str__() and __call__() Methods
# TIMESTAMP__2024_08_04__115117
# This example demonstrates the use of __str__() and __call__() methods in a library management system.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __call__(self):
        for book in self.books:
            print(book)


# Create book instances
book1 = Book("Python Programming", "John Doe", 2021)
book2 = Book("Learning Python", "Jane Doe", 2019)

# Create a library instance and add books to it
library = Library()
library.add_book(book1)
library.add_book(book2)

# Print the book details using __str__() method
print(book1)  # Output: Python Programming by John Doe (2021)

# Call the library instance like a function using __call__() method
library()  # Output: Details of all books in the library
