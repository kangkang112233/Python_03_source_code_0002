# This code example demonstrates the usage of special characters in regex
# in the context of a library management system.

import re


def find_books(pattern, book_titles):
    """
    Find books that match the given regex pattern.

    Args:
    pattern (str): The regex pattern to be matched.
    book_titles (list): A list of book titles.

    Returns:
    list: A list of book titles that match the pattern.
    """
    matching_books = []
    for title in book_titles:
        if re.search(pattern, title):
            matching_books.append(title)
    return matching_books


# Book titles in the library
book_titles = [
    "Learning Python",
    "Mastering Data Science",
    "Introduction to AI",
    "Advanced C++ Programming",
    "Data Structures and Algorithms",
]

# Patterns to search
pattern_any_char = "P.thon"  # . matches any single character
pattern_char_set = "[Dd]ata"  # [Dd] matches 'D' or 'd'
pattern_one_or_more = "A.+"  # A.+ matches 'A' followed by one or more characters

# Find books
books_any_char = find_books(pattern_any_char, book_titles)
books_char_set = find_books(pattern_char_set, book_titles)
books_one_or_more = find_books(pattern_one_or_more, book_titles)

# Display results
print("Books matching pattern 'P.thon':")
for book in books_any_char:
    print(book)

print("\nBooks matching pattern '[Dd]ata':")
for book in books_char_set:
    print(book)

print("\nBooks matching pattern 'A.+':")
for book in books_one_or_more:
    print(book)
