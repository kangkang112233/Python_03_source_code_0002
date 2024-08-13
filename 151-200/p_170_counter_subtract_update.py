# Explanation of subtract() and update() Methods in Python's collections.Counter
# TIMESTAMP__2024_08_12__123257

from collections import Counter


# Function to demonstrate subtract() and update() methods
def demonstrate_counter_operations():
    counter = Counter({"apple": 3, "banana": 2, "orange": 1})

    print("Original counter:")
    print(counter)

    # Subtract elements
    counter.subtract({"apple": 1, "banana": 2, "pear": 1})
    print("\nCounter after subtracting {'apple': 1, 'banana': 2, 'pear': 1}:")
    print(counter)

    # Update elements
    counter.update({"apple": 2, "orange": 3, "grape": 4})
    print("\nCounter after updating {'apple': 2, 'orange': 3, 'grape': 4}:")
    print(counter)


demonstrate_counter_operations()
