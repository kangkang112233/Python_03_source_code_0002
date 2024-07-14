# Book management system example demonstrating manual __eq__ method


class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    # Manually defining the __eq__ method
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.book_id == other.book_id
            and self.title == other.title
            and self.author == other.author
            and self.price == other.price
        )

    # Defining the __repr__ method
    def __repr__(self):
        return (
            f"Book(book_id={self.book_id}, title='{self.title}', "
            f"author='{self.author}', price={self.price})"
        )


# Creating book instances with the same and different values
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(1, "1984", "George Orwell", 19.99)
book3 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Accessing and printing book details
print(f"Book 1: {book1}")
print(f"Book 2: {book2}")
print(f"Book 3: {book3}")

# Comparing books
print(f"Are book1 and book2 the same? {'Yes' if book1 == book2 else 'No'}")
print(f"Are book1 and book3 the same? {'Yes' if book1 == book3 else 'No'}")


# Creating a library class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book {book.title} added to {self.name} library."

    def __repr__(self):
        return f"Library(name={self.name}, books={self.books})"


# Creating a library instance
library = Library("Central Library")

# Adding books to the library
print(library.add_book(book1))
print(library.add_book(book3))

# Printing the books in the library
print("\nBooks in Central Library:")
for book in library.books:
    print(
        f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Price: {book.price}"
    )
