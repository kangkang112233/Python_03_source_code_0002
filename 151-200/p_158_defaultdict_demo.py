# Explanation of defaultdict in Python
# TIMESTAMP__2024_08_11__121704

from collections import defaultdict


# Function to count the number of books by each author in a library system
def count_books_by_author(library):
    author_count = defaultdict(int)
    for book in library:
        author_count[book["author"]] += 1
    return author_count


# Example library list
library = [
    {"title": "Python Programming", "author": "John Doe"},
    {"title": "Data Science with Python", "author": "Jane Smith"},
    {"title": "Machine Learning Basics", "author": "John Doe"},
]

# Counting books by each author
author_book_counts = count_books_by_author(library)

# Printing the count of books by each author
print("Count of books by each author:")
for author, count in author_book_counts.items():
    print(f"Author: {author}, Number of Books: {count}")
