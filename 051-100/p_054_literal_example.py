# Book management system example demonstrating the use of Literal in type hints

from typing import Literal
from dataclasses import dataclass


def set_book_condition(condition: Literal["new", "used", "refurbished"]):
    if condition == "new":
        return "The book is in new condition."
    elif condition == "used":
        return "The book is in used condition."
    elif condition == "refurbished":
        return "The book is in refurbished condition."
    else:
        raise ValueError("Invalid condition")


# Setting book conditions
print(set_book_condition("new"))
print(set_book_condition("used"))
print(set_book_condition("refurbished"))
# print(set_book_condition("aaaaaaaaaaaaSS"))

# Example of using Literal in a dataclass for a library system


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    condition: Literal["new", "used", "refurbished"]


# Creating book instances with specific conditions
book1 = Book(1, "1984", "George Orwell", "new")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "used")
book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "refurbished")

# Printing book details
print(book1)
print(book2)
print(book3)
