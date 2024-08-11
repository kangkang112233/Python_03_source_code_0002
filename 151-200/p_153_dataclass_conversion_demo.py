# Explanation of dataclasses module's asdict and astuple functions
# TIMESTAMP__2024_08_11__111833

from dataclasses import dataclass, asdict, astuple


@dataclass
class Book:
    title: str
    author: str
    year: int


# Example book object
book = Book(title="Python Programming", author="John Doe", year=2020)

# Convert the book object to a dictionary
book_dict = asdict(book)
print("Book as dictionary:", book_dict)

# Convert the book object to a tuple
book_tuple = astuple(book)
print("Book as tuple:", book_tuple)
