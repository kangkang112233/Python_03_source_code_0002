# Import necessary module
from collections import Counter

# List of books borrowed by users
borrowed_books = [
    "The Catcher in the Rye",
    "1984",
    "To Kill a Mockingbird",
    "The Catcher in the Rye",
    "1984",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "1984",
    "The Catcher in the Rye",
    "To Kill a Mockingbird",
]

# Use Counter to count the occurrences of each book
book_counter = Counter(borrowed_books)

# Print the count of each book
print("Count of each borrowed book:")
for book, count in book_counter.items():
    print(f"{book}: {count} times")
