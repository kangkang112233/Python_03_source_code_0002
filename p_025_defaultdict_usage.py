# Import necessary module
from collections import defaultdict

# List of borrowed books with their authors
borrowed_books = [
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Pride and Prejudice", "Jane Austen"),
    ("Animal Farm", "George Orwell"),
    ("The Catcher in the Rye", "J.D. Salinger"),
]

# Use defaultdict to group books by author
books_by_author = defaultdict(list)

# Populate the defaultdict with books
for title, author in borrowed_books:
    books_by_author[author].append(title)

# Print the list of books for each author
print("Books borrowed by each author:")
for author, titles in books_by_author.items():
    print(f"{author}:")
    for title in titles:
        print(f"  - {title}")
