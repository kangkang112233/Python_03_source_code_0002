# This code example demonstrates the usage of the isalpha() method
# in the context of a library management system.


def check_book_title(title):
    """
    Check if the book title contains only alphabetic characters.

    Args:
    title (str): The book title to be checked.

    Returns:
    bool: True if the title contains only alphabetic characters, False otherwise.
    """
    return title.isalpha()


# Test cases
book_title1 = "PythonProgramming"
book_title2 = "Python Programming 101"
book_title3 = "プログラミング"

# Check book titles
print(f"Is '{book_title1}' alphabetic only? {check_book_title(book_title1)}")
print(f"Is '{book_title2}' alphabetic only? {check_book_title(book_title2)}")
print(f"Is '{book_title3}' alphabetic only? {check_book_title(book_title3)}")
