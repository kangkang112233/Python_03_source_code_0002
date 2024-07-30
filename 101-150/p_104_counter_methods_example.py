# Knowledge point: subtract() and update() methods

from collections import Counter


# Example for a library management system
# Function to update and subtract book counts
def manage_book_counts():
    library_counts = Counter({"1984": 4, "Brave New World": 2, "Fahrenheit 451": 3})

    # Books to add to the library
    new_books = {"1984": 2, "The Handmaid's Tale": 3}
    library_counts.update(new_books)

    # Books to remove from the library
    books_to_remove = {"1984": 1, "Brave New World": 1, "Fahrenheit 451": 4}
    library_counts.subtract(books_to_remove)

    return library_counts


# Function to display the book counts
def display_book_counts(counts):
    print("Current book counts in the library:")
    for book, count in counts.items():
        print(f"{book}: {count}")


# Example usage
if __name__ == "__main__":
    counts = manage_book_counts()
    display_book_counts(counts)

# Output:
# Current book counts in the library:
# 1984: 5
# Brave New World: 1
# Fahrenheit 451: -1
# The Handmaid's Tale: 3
