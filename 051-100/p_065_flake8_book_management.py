import json


class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.to_dict() for book in self.books]

    def save_books(self, filename):
        with open(filename, "w") as file:
            json.dump(self.list_books(), file, indent=4)

    def load_books(self, filename):
        with open(filename, "r") as file:
            books = json.load(file)
            self.books = [Book(**book) for book in books]


# Example usage
library = Library()
library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"))

# Save books to a file
library.save_books("books.json")

# Load books from a file
library.load_books("books.json")

# Print list of books
for book in library.list_books():
    print(f"Title: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\n")
