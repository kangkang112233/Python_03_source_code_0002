# Knowledge Point: @enum.unique decorator

import enum


# Apply the @enum.unique decorator to ensure all enum values are unique
@enum.unique
class BookStatus(enum.Enum):
    AVAILABLE = "Available"
    CHECKED_OUT = "Checked Out"
    LOST = "Lost"
    # Uncommenting the line below would raise an error because "Available" is already used.
    # RESERVED = "Available"


# Function to print the status of a book
def print_book_status(status):
    if status == BookStatus.AVAILABLE:
        print("The book is available.")
    elif status == BookStatus.CHECKED_OUT:
        print("The book is checked out.")
    elif status == BookStatus.LOST:
        print("The book is lost.")
    else:
        print("Unknown status.")


# Example usage
print_book_status(BookStatus.AVAILABLE)
print_book_status(BookStatus.CHECKED_OUT)
print_book_status(BookStatus.LOST)
