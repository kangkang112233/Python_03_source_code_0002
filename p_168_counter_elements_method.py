# Explanation of elements() Method in Python's collections.Counter
# TIMESTAMP__2024_08_12__121935

from collections import Counter


# Function to demonstrate elements() method
def demonstrate_elements(counter):
    after_change = counter.elements()
    print(type(after_change))
    change_to_list = list(after_change)
    return change_to_list


# Example counter
counter = Counter({"apple": 3, "banana": -1, "orange": 2, "pear": 0})

# Using the elements() method
elements_list = demonstrate_elements(counter)

print("Elements returned by the elements() method:")
print(elements_list)
