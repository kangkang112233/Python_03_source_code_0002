# This script demonstrates the use of list comprehensions with if statements in a book management system.
# Application context: Filtering books based on a condition


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


# Creating a list of books
books = [
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
    Book("Brave New World", "Aldous Huxley", 1932),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
]

# Using list comprehension to filter books published after 1950
books_after_1950 = [book.title for book in books if book.year > 1950]

print("Books published after 1950:")
for title in books_after_1950:
    print(f"- {title}")

# Using list comprehension to filter books by a specific author
author = "George Orwell"
books_by_author = [book.title for book in books if book.author == author]

print(f"\nBooks by {author}:")
for title in books_by_author:
    print(f"- {title}")
