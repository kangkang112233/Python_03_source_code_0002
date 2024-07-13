# Book management system example demonstrating instance, class, and static methods


class Library:
    # Class variable to keep track of the total number of books in all libraries
    total_books = 0

    def __init__(self, name):
        # Instance variable to store the library's name
        self.name = name
        # Instance variable to store the list of books in this library
        self.books = []

    # Instance method
    def add_book(self, book):
        self.books.append(book)
        Library.total_books += 1
        return f"Book {book['title']} added to {self.name} library."

    # Instance method
    def remove_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                Library.total_books -= 1
                return f"Book {book['title']} removed from {self.name} library."
        return "Book not found."

    # Class method
    @classmethod
    def get_total_books(cls):
        return f"Total books in all libraries: {cls.total_books}"

    # Static method
    @staticmethod
    def is_valid_book(book):
        return "id" in book and "title" in book and "author" in book


# Creating instances of Library
library1 = Library("Central")
library2 = Library("East Branch")

# Adding books to libraries
print(library1.add_book({"id": 1, "title": "Book Title 1", "author": "Author A"}))
print(library2.add_book({"id": 2, "title": "Book Title 2", "author": "Author B"}))
print(library1.add_book({"id": 3, "title": "Book Title 3", "author": "Author A"}))

# Removing a book from a library
print(library1.remove_book(1))

# Printing the total number of books in all libraries using class method
print(Library.get_total_books())

# Printing the books in each library
print("\nBooks in Central Library:")
for book in library1.books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

print("\nBooks in East Branch Library:")
for book in library2.books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

# Validating book using static method
print("\nValidating books:")
book = {"id": 4, "title": "Book Title 4", "author": "Author D"}
print(f"Is valid book: {Library.is_valid_book(book)}")
