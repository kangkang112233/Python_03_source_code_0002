# Explanation of permutations, combinations, product, and combinations_with_replacement
# TIMESTAMP__2024_08_11__122647

from itertools import permutations, combinations, product, combinations_with_replacement

# Example list of book genres
genres = ["Fiction", "Non-Fiction", "Science"]

# Generating all permutations of genres
print("Permutations of genres:")
for p in permutations(genres):
    print(p)

# Generating all combinations of genres (2 at a time)
print("\nCombinations of genres (2 at a time):")
for c in combinations(genres, 2):
    print(c)

# Generating the Cartesian product of genres with itself
print("\nCartesian product of genres with itself:")
for prod in product(genres, repeat=2):
    print(prod)

# Generating all combinations with replacement (2 at a time)
print("\nCombinations with replacement of genres (2 at a time):")
for cr in combinations_with_replacement(genres, 2):
    print(cr)
