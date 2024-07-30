# Knowledge point: elements() method of collections.Counter

from collections import Counter


# Example for a library management system
# Function to list all books with their counts using Counter
def list_books_with_counts(books):
    book_counter = Counter(books)

    # Get an iterator that repeats each element as many times as its count
    book_elements = list(book_counter.elements())

    return book_elements


# Function to display the list of books
def display_books(book_elements):
    print("Books in the library (repeated by count):")
    for book in book_elements:
        print(book)


# Example usage
if __name__ == "__main__":
    books = [
        "1984",
        "Brave New World",
        "1984",
        "To Kill a Mockingbird",
        "1984",
        "Brave New World",
        "Fahrenheit 451",
    ]
    book_elements = list_books_with_counts(books)
    display_books(book_elements)

# Output:
# Books in the library (repeated by count):
# 1984
# 1984
# 1984
# Brave New World
# Brave New World
# To Kill a Mockingbird
# Fahrenheit 451
