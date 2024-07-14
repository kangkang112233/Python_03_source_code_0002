# Book management system example demonstrating the use of super() function


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book {book['title']} added to {self.name} library."


class DigitalLibrary(Library):
    def __init__(self, name, website):
        # Use super() to call the __init__ method of the parent class
        super().__init__(name)
        self.website = website

    def add_book(self, book):
        # Use super() to call the add_book method of the parent class
        result = super().add_book(book)
        return f"{result} The book is also available online at {self.website}."


# Creating instances of Library and DigitalLibrary
library1 = Library("Central Library")
digital_library1 = DigitalLibrary("Central Digital Library", "www.centraldigital.com")

# Adding books to libraries
print(library1.add_book({"id": 1, "title": "Book Title 1", "author": "Author A"}))
print(
    digital_library1.add_book(
        {"id": 2, "title": "Digital Book Title 1", "author": "Author B"}
    )
)

# Printing the books in each library
print("\nBooks in Central Library:")
for book in library1.books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

print("\nBooks in Central Digital Library:")
for book in digital_library1.books:
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
