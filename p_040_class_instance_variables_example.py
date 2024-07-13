# Book management system example demonstrating class and instance variables


class Library:
    # Class variable
    total_books = 0

    def __init__(self, name):
        # Instance variable
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1
        return f"Book {book['title']} added to {self.name} library."

    def remove_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                Library.total_books -= 1
                return f"Book {book['title']} removed from {self.name} library."
        return "Book not found."


# Creating instances of Library
library1 = Library("Central")
library2 = Library("East Branch")

# Adding books to libraries
print(library1.add_book({"id": 1, "title": "Book Title 1", "author": "Author A"}))
print(library2.add_book({"id": 2, "title": "Book Title 2", "author": "Author B"}))
print(library1.add_book({"id": 3, "title": "Book Title 3", "author": "Author A"}))

# Removing a book from a library
print(library1.remove_book(1))

# Printing the total number of books in all libraries
print(f"Total books in all libraries: {Library.total_books}")

# Printing the books in each library
print("\nBooks in Central Library:")
for book in library1.books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

print("\nBooks in East Branch Library:")
for book in library2.books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
