# Explanation of the yield statement and generator objects
# TIMESTAMP__2024_08_11__105933


# Function to generate book titles in the library one by one using a generator
def generate_book_titles(library):
    for book in library:
        yield book["title"]


# Example library list
library = [
    {"title": "Python Programming", "author": "John Doe"},
    {"title": "Data Science with Python", "author": "Jane Smith"},
    {"title": "Machine Learning Basics", "author": "Alan Turing"},
]

# Using the generator to print each book title with next() function
book_titles = generate_book_titles(library)
print(f"Book title: {next(book_titles)}")
print(f"Book title: {next(book_titles)}")
print(f"Book title: {next(book_titles)}")

# Handling StopIteration exception when no more items are available
try:
    print(f"Book title: {next(book_titles)}")
except StopIteration:
    print("No more books in the library.")
