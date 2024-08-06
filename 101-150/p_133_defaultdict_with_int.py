# Using defaultdict with int
# TIMESTAMP__2024_08_04__121641
# This example demonstrates how to use defaultdict with int in a library management system.

from collections import defaultdict

# Create a defaultdict with int, default value will be 0
book_counts = defaultdict(int)

# Increment counts for different books
book_counts["Python Programming"] += 1
book_counts["Learning Python"] += 2

# Display the book counts
for book, count in book_counts.items():
    print(f"{book}: {count}")

# Accessing a non-existent key
print(f"Non-existent book count: {book_counts['Effective Python']}")
