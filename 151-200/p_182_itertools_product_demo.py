# Explanation of itertools.product in Python
# TIMESTAMP__2024_08_13__103315

import itertools

# Sample lists
list1 = ["A", "B", "C"]
list2 = [1, 2]

# Using itertools.product
print("Using itertools.product:")
for p in itertools.product(list1, list2):
    print(p)

# Equivalent nested for loops
print("\nUsing nested for loops:")
for a in list1:
    for b in list2:
        print((a, b))
