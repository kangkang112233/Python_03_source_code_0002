# Knowledge point: elements() method of collections.Counter with negative counts

from collections import Counter


# Example to demonstrate elements() and negative counts
def demonstrate_counter_behavior():
    # Create a Counter with some positive and negative counts
    book_counts = Counter(
        {
            "1984": 3,
            "Brave New World": 2,
            "To Kill a Mockingbird": 1,
            "Fahrenheit 451": -1,
        }
    )

    # Get elements, which will ignore the negative count
    book_elements = list(book_counts.elements())

    # Get items, which include the counts
    book_items = list(book_counts.items())

    return book_elements, book_items


# Function to display the results
def display_results(book_elements, book_items):
    print("Books in the library (repeated by count):")
    for book in book_elements:
        print(book)

    print("\nBooks with their counts:")
    for book, count in book_items:
        print(f"{book}: {count}")


# Example usage
if __name__ == "__main__":
    book_elements, book_items = demonstrate_counter_behavior()
    display_results(book_elements, book_items)

# Expected Output:
# Books in the library (repeated by count):
# 1984
# 1984
# 1984
# Brave New World
# Brave New World
# To Kill a Mockingbird

# Books with their counts:
# 1984: 3
# Brave New World: 2
# To Kill a Mockingbird: 1
# Fahrenheit 451: -1
