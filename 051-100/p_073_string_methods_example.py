# This code example demonstrates the usage of swapcase(), normalize(), title(), and capitalize()
# in the context of a library management system.

import unicodedata


def process_book_title(title):
    """
    Process the book title using various string methods.

    Args:
    title (str): The book title to be processed.

    Returns:
    dict: A dictionary with the results of various string methods.
    """
    results = {
        "original": title,
        "swapcase": title.swapcase(),  # Swap uppercase and lowercase letters
        "normalized": unicodedata.normalize("NFKC", title),  # Normalize Unicode string
        "title": title.title(),  # Capitalize the first letter of each word
        "capitalize": title.capitalize(),  # Capitalize the first letter of the string
    }
    return results


# Test cases
book_titles = [
    "Learning PYTHON",
    "Mastering data science",
    "introduction to AI",
    "advanced c++ programming",
]

# Process book titles
for book_title in book_titles:
    results = process_book_title(book_title)
    print(f"Original: {results['original']}")
    print(f"Swapcase: {results['swapcase']}")
    print(f"Normalized: {results['normalized']}")
    print(f"Title: {results['title']}")
    print(f"Capitalize: {results['capitalize']}")
    print("\n")
