# Explanation of most_common() Method in Python's collections.Counter
# TIMESTAMP__2024_08_12__122653

from collections import Counter


# Function to demonstrate most_common() method
def demonstrate_most_common(counter, n=None):
    return counter.most_common(n)


# Example counter
counter = Counter({"apple": 3, "banana": 5, "orange": 2, "pear": 4})

# Using the most_common() method without argument
most_common_all = demonstrate_most_common(counter)

# Using the most_common() method with argument
most_common_two = demonstrate_most_common(counter, 2)

print("Most common elements (all):")
print(most_common_all)

print("\nMost common elements (top 2):")
print(most_common_two)
