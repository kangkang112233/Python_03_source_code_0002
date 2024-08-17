# Explanation of itertools Functions in Python
# TIMESTAMP__2024_08_13__102711

import itertools

# Sample list
data = ["A", "B", "C"]

# Permutations
print("Permutations:")
for p in itertools.permutations(data):
    print(p)

# Combinations
print("\nCombinations (length 2):")
for c in itertools.combinations(data, 2):
    print(c)

# Product
print("\nCartesian Product:")
for p in itertools.product(data, repeat=2):
    print(p)

# Combinations with replacement
print("\nCombinations with Replacement (length 2):")
for c in itertools.combinations_with_replacement(data, 2):
    print(c)
