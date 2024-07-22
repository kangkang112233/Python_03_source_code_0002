# This script demonstrates the use of set comprehension and dictionary comprehension.
# Application context: Managing a library system with books and their availability

# List of books with availability status
books = [
    ("The Catcher in the Rye", True),
    ("To Kill a Mockingbird", False),
    ("1984", True),
    ("Brave New World", True),
    ("The Great Gatsby", False),
]

# Using set comprehension to create a set of available books
available_books = {book for book, available in books if available}

print("Available Books:")
for book in available_books:
    print(f"- {book}")

print("\n")  # Newline for better readability

# Using dictionary comprehension to create a dictionary with book availability
books_dict = {book: available for book, available in books if available}

print("Books Availability Dictionary:")
for book, available in books_dict.items():
    status = "Available" if available else "Not Available"
    print(f"- {book}: {status}")
