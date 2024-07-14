# Book management system example demonstrating the use of str.find()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for index, book in enumerate(self.books):
            if book.title.find(title) != -1:
                return index
        return -1


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book[ID: {self.book_id}, Title: {self.title}, Author: {self.author}]"


# Creating book instances
book1 = Book(1, "1984", "George Orwell")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald")

# Creating a library instance and adding books to it
library = Library("Central Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Searching for books by title
print("Searching for '1984':", library.find_book("1984"))  # Should return 0
print(
    "Searching for 'Mockingbird':", library.find_book("Mockingbird")
)  # Should return 1
print("Searching for 'Moby Dick':", library.find_book("Moby Dick"))  # Should return -1

# Printing book details
print("\nBooks in the library:")
for book in library.books:
    print(book)
