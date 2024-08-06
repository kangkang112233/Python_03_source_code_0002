# Type Hints in Python
# TIMESTAMP__2024_08_04__114605
# This example demonstrates the use of type hints in a library management system.

from typing import List, Dict, Tuple


def get_book_titles() -> List[str]:
    return ["Python Programming", "Learning Python", "Effective Python"]


def get_book_details() -> Dict[str, int]:
    return {
        "Python Programming": 2021,
        "Learning Python": 2019,
        "Effective Python": 2015,
    }


def get_book_info() -> Tuple[str, str, int]:
    return ("Python Programming", "John Doe", 2021)


# Using the functions
titles = get_book_titles()
details = get_book_details()
info = get_book_info()

print("Book Titles:", titles)
print("Book Details:", details)
print("Book Info:", info)
