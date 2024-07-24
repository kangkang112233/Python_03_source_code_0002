# This code example demonstrates how assigning objects to variables works
# in the context of a library management system.


def modify_book_list(book_list):
    """
    Modify the book list by adding a new book.

    Args:
    book_list (list): The original list of book titles.

    Returns:
    None
    """
    book_list.append("New Book")  # Modify the book list by adding a new book


# Original book list
original_books = ["Learning Python", "Mastering Data Science", "Introduction to AI"]

# Assign the original book list to another variable
assigned_books = original_books

# Modify the assigned book list
modify_book_list(assigned_books)

# Display results
print("Original book list after modification:")
print(original_books)

print("\nAssigned book list after modification:")
print(assigned_books)
