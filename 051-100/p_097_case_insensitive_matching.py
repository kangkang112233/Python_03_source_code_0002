# Knowledge point: re.I and re.IGNORECASE for case-insensitive matching

import re


# Example for a library management system
# Function to search for a book title in a case-insensitive manner
def search_book_title(library, title_pattern):
    # Compile the regular expression pattern with the re.IGNORECASE flag
    pattern = re.compile(title_pattern, re.IGNORECASE)

    # Search for the pattern in the library's book titles
    matched_books = [book for book in library if pattern.search(book)]

    return matched_books


# Example usage
def main():
    library = [
        "1984",
        "Brave New World",
        "Fahrenheit 451",
        "The Handmaid's Tale",
        "To Kill a Mockingbird",
    ]
    title_pattern = "new"

    # Search for books with titles that match the pattern, ignoring case
    results = search_book_title(library, title_pattern)

    print("Books matching the pattern:")
    for book in results:
        print(book)


if __name__ == "__main__":
    main()

# Output:
# Books matching the pattern:
# Brave New World
