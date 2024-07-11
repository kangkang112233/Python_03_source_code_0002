# Import necessary module
from operator import attrgetter


# Define a class for books
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Create a list of book instances
books = [
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("Pride and Prejudice", "Jane Austen", 1813),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
]

# Sort books by author name
sorted_books_by_author = sorted(books, key=attrgetter("author"))
print("Books sorted by author:")
for book in sorted_books_by_author:
    print(book)

# Sort books by publication year
sorted_books_by_year = sorted(books, key=attrgetter("year"))
print("\nBooks sorted by year:")
for book in sorted_books_by_year:
    print(book)

# Sort books by title
sorted_books_by_title = sorted(books, key=attrgetter("title"))
print("\nBooks sorted by title:")
for book in sorted_books_by_title:
    print(book)
