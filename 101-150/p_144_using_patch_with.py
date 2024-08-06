# Using patch with with in Python
# TIMESTAMP__2024_08_04__170826
# This example demonstrates how to use patch with with in a library management system.

from unittest.mock import patch


# Sample function to be tested
def get_book_data():
    # Simulate a function that fetches book data from an external source
    return {"title": "Python Programming", "author": "John Doe", "year": 2021}


# Test function using patch
def test_get_book_data():
    with patch(
        "__main__.get_book_data",
        return_value={"title": "Mocked Book", "author": "Jane Doe", "year": 2022},
    ):
        book_data = get_book_data()
        print("Mocked book data:", book_data)


if __name__ == "__main__":
    test_get_book_data()
