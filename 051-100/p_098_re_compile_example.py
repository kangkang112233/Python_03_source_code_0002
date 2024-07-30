# Knowledge point: re.compile

import re


# Example for a library management system
# Function to search for books by title using a compiled regular expression
def search_books(library, pattern):
    # Compile the regular expression pattern
    regex = re.compile(pattern, re.IGNORECASE)  # Ignore case for matching

    # Search for matching books in the library
    matched_books = [book for book in library if regex.search(book)]

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
    pattern = "new"

    # Search for books matching the pattern
    results = search_books(library, pattern)

    print("Books matching the pattern:")
    for book in results:
        print(book)


if __name__ == "__main__":
    main()

# Output:
# Books matching the pattern:
# Brave New World
