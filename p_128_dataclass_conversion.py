# Converting Dataclass Instances
# TIMESTAMP__2024_08_04__113217
# This example demonstrates how to convert dataclass instances to dictionaries and tuples in a library management system.

from dataclasses import dataclass, asdict, astuple


@dataclass
class Book:
    title: str
    author: str
    year: int


# Create an instance of the Book dataclass
book = Book(title="Python Programming", author="John Doe", year=2021)

# Convert the dataclass instance to a dictionary
book_dict = asdict(book)
print("Dataclass instance as dictionary:\n", book_dict)

# Convert the dataclass instance to a tuple
book_tuple = astuple(book)
print("\nDataclass instance as tuple:\n", book_tuple)
