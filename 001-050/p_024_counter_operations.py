# Import necessary module
from collections import Counter

# Define borrowed books from two different branches
branch1_borrowed_books = [
    "The Catcher in the Rye",
    "1984",
    "To Kill a Mockingbird",
    "The Catcher in the Rye",
    "1984",
]

branch2_borrowed_books = [
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "1984",
    "To Kill a Mockingbird",
]

# Create Counter objects for each branch
counter1 = Counter(branch1_borrowed_books)
counter2 = Counter(branch2_borrowed_books)

# Add counts from both branches
total_borrowed_books = counter1 + counter2
print("Total borrowed books from both branches:")
for book, count in total_borrowed_books.items():
    print(f"{book}: {count} times")

# Subtract counts of branch2 from branch1
difference_borrowed_books = counter1 - counter2
print("\nBooks borrowed more in branch1 than branch2:")
for book, count in difference_borrowed_books.items():
    print(f"{book}: {count} times")

# Find common minimum borrowed books (intersection)
common_min_borrowed_books = counter1 & counter2
print("\nCommon minimum borrowed books in both branches:")
for book, count in common_min_borrowed_books.items():
    print(f"{book}: {count} times")

# Find common maximum borrowed books (union)
common_max_borrowed_books = counter1 | counter2
print("\nCommon maximum borrowed books in both branches:")
for book, count in common_max_borrowed_books.items():
    print(f"{book}: {count} times")
