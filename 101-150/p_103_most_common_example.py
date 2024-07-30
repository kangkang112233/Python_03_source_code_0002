# Knowledge point: most_common() method returns a list

from collections import Counter


# Example for a library management system
# Function to get the most common books
def get_most_common_books(books, n):
    book_counter = Counter(books)

    # Get the most common books as a list of tuples
    most_common_books = book_counter.most_common(n)
    print(type(most_common_books))
    print(most_common_books)

    return most_common_books


# Function to display the most common books
def display_most_common_books(most_common_books):
    print("Most common books in the library:")
    for book, count in most_common_books:
        print(f"{book}: {count}")


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
    n = 2  # Number of most common books to retrieve
    most_common_books = get_most_common_books(books, n)
    display_most_common_books(most_common_books)

# Output:
# Most common books in the library:
# 1984: 3
# Brave New World: 2
