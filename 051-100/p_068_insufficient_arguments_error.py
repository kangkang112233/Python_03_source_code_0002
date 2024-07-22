# This script demonstrates an error due to insufficient arguments during class instantiation.
# Application context: Managing a library system with books


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Correct instantiation with all required arguments
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
print(book1.display_info())

# Incorrect instantiation with missing arguments
try:
    book2 = Book("To Kill a Mockingbird")  # Missing author and year
except TypeError as e:
    print(f"Error: {e}")

# Correct instantiation after fixing the error
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book2.display_info())
