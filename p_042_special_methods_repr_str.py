# Book management system example demonstrating __repr__ and __str__ methods


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    # Defining the __repr__ method
    def __repr__(self):
        return f"Book(book_id={self.book_id}, title='{self.title}', author='{self.author}')"

    # Defining the __str__ method
    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Creating book instances
book1 = Book(1, "1984", "George Orwell")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")

# Using repr() to get the official string representation
print(repr(book1))
print(repr(book2))

# Using str() to get the informal string representation
print(str(book1))
print(str(book2))

# Printing the book objects directly, which calls the __str__ method
print(book1)
print(book2)
