# This code example demonstrates how to use the enum module with auto()
# to automatically assign consecutive numbers to enumeration constants
# in the context of a library management system.

from enum import Enum, auto


class BookCategory(Enum):
    """
    Enumeration for book categories with automatic numbering.
    """

    FICTION = auto()
    NON_FICTION = auto()
    SCIENCE = auto()
    ART = auto()
    TECHNOLOGY = auto()


def display_book_categories():
    """
    Display the book categories and their auto-assigned values.

    Returns:
    None
    """
    for category in BookCategory:
        print(f"{category.name} = {category.value}")


# Display book categories
display_book_categories()
