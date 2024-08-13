# Explanation of MagicMock Methods assert_called_once and assert_called_with in Python
# TIMESTAMP__2024_08_12__131512

from unittest.mock import MagicMock


# Example of a library management system
class Library:
    def __init__(self):
        self.inventory = {}

    def add_book(self, book, quantity):
        if book in self.inventory:
            self.inventory[book] += quantity
        else:
            self.inventory[book] = quantity

    def borrow_book(self, book, borrower):
        if self.inventory.get(book, 0) > 0:
            self.inventory[book] -= 1
            self.notify_borrow(book, borrower)
        else:
            raise ValueError("Book not available")

    def notify_borrow(self, book, borrower):
        # This function would send a notification to the borrower
        print(f"Notification sent to {borrower} for borrowing {book}")


# Testing the Library class using MagicMock
def test_library_borrow_book():
    library = Library()
    library.add_book("Python Programming", 3)

    # Mock the notify_borrow method
    library.notify_borrow = MagicMock()

    # Borrow a book
    library.borrow_book("Python Programming", "John Doe")

    # Asserting that notify_borrow was called exactly once
    try:
        library.notify_borrow.assert_called_once()
        print("notify_borrow was called exactly once.")
    except AssertionError:
        print("notify_borrow was not called exactly once.")

    # Asserting that notify_borrow was called with specific arguments
    try:
        library.notify_borrow.assert_called_with("Python Programming", "John Doe")
        print("notify_borrow was called with the correct arguments.")
    except AssertionError:
        print("notify_borrow was not called with the correct arguments.")


test_library_borrow_book()
