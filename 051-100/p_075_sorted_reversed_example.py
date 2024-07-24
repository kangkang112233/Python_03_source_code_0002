# This code example demonstrates the usage of sorted() and reversed()
# in the context of a library management system.


def sort_books(books):
    """
    Sort the list of books in descending order.

    Args:
    books (list): A list of book titles.

    Returns:
    list: A new list of book titles sorted in descending order.
    """
    return sorted(books, reverse=True)  # Sort books in descending order


def reverse_books(books):
    """
    Reverse the list of books.

    Args:
    books (list): A list of book titles.

    Returns:
    list: A new list of book titles in reversed order.
    """
    return list(reversed(books))  # Reverse the order of books


# Test cases
book_titles = [
    "Learning Python",
    "Mastering Data Science",
    "Introduction to AI",
    "Advanced C++ Programming",
    "Data Structures and Algorithms",
]

# Sort and reverse books
sorted_books = sort_books(book_titles)
reversed_books = reverse_books(book_titles)

# Display results
print("Original book titles:")
print(book_titles)

print("\nSorted book titles (descending):")
print(sorted_books)

print("\nReversed book titles:")
print(reversed_books)
