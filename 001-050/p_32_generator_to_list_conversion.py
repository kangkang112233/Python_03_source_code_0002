# Book management system example showing issues with multiple iteration of generator


# Generator function to filter books by author
def filter_books_by_author(books, author_name):
    for book in books:
        if book["author"] == author_name:
            yield book


# List of books as a sample data
books = [
    {"id": 1, "title": "Book Title 1", "author": "Author A"},
    {"id": 2, "title": "Book Title 2", "author": "Author B"},
    {"id": 3, "title": "Book Title 3", "author": "Author A"},
    {"id": 4, "title": "Book Title 4", "author": "Author C"},
    {"id": 5, "title": "Book Title 5", "author": "Author B"},
]

# Create a generator object to filter books by "Author A"
author_a_books = filter_books_by_author(books, "Author A")

# Get and print books for the first time
print("First iteration:")
for book in author_a_books:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")

# Attempt to get and print books for the second time using the same generator object
print("\nSecond iteration:")
try:
    # This will not print anything because the generator is exhausted
    for book in author_a_books:
        print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
    if not any(author_a_books):
        print("No books found - the generator is exhausted.")
except Exception as e:
    print(f"Error: {e}")

# Convert the generator to a list for reuse
author_a_books_list = list(filter_books_by_author(books, "Author A"))

print("\nUsing the list to print books again:")
for book in author_a_books_list:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
