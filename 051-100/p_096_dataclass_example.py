# Knowledge point: Using dataclass with type hints

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int


@dataclass
class Library:
    name: str
    books: list

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def list_books(self):
        print(f"Listing books in {self.name}:")
        for book in self.books:
            print(f"{book.title} by {book.author}, published in {book.year}")


# Example usage
def main():
    library = Library(name="City Library", books=[])
    book1 = Book(title="1984", author="George Orwell", year=1949)
    book2 = Book(title="Brave New World", author="Aldous Huxley", year=1932)

    library.add_book(book1)
    library.add_book(book2)

    library.list_books()


if __name__ == "__main__":
    main()

# Output:
# Book '1984' by George Orwell added to the library.
# Book 'Brave New World' by Aldous Huxley added to the library.
# Listing books in City Library:
# 1984 by George Orwell, published in 1949
# Brave New World by Aldous Huxley, published in 1932
