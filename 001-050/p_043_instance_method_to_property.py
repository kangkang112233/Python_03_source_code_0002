# Book management system example demonstrating how to turn an instance method into a property


class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self._price = price  # Price is a protected attribute

    # Defining a property for price
    @property
    def price(self):
        return self._price

    # Setter for the price property
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Defining the __repr__ method
    def __repr__(self):
        return f"Book(book_id={self.book_id}, title='{self.title}', author='{self.author}', price={self._price})"


# Creating book instances
book1 = Book(1, "1984", "George Orwell", 19.99)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", 9.99)

# Accessing and modifying the price using the property
print(f"Initial price of '{book1.title}': ${book1.price}")
book1.price = 21.99
print(f"Updated price of '{book1.title}': ${book1.price}")

# Attempting to set a negative price
try:
    book1.price = -5.99
except ValueError as e:
    print(e)

# Printing the book objects to see the updated prices
print(book1)
print(book2)
print(book1._price)
