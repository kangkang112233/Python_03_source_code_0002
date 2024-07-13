# Book management system example showing generator usage and ensuring actions are executed


# Sample database update function
def db_update(book):
    print(f"Updating database with: {book}")


# Generator function to process books
def process_books(books):
    for book in books:
        db_update(book)  # Simulate database update
        yield book


# List of books as a sample data
books = [
    {"id": 1, "title": "Book Title 1", "author": "Author A"},
    {"id": 2, "title": "Book Title 2", "author": "Author B"},
    {"id": 3, "title": "Book Title 3", "author": "Author A"},
    {"id": 4, "title": "Book Title 4", "author": "Author C"},
    {"id": 5, "title": "Book Title 5", "author": "Author B"},
]

# Create a generator object
book_gen = process_books(books)

# Ensure the generator runs and db_update is executed
print("Processing books:")
for book in book_gen:
    print(
        f"Processed Book - ID: {book['id']}, Title: {book['title']}, Author: {book['author']}\n"
    )

# Convert the generator to a list to ensure all updates are processed
book_list = list(process_books(books))

print("\nProcessed books from list:")
for book in book_list:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
