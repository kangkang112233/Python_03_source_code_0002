# Explanation of zip() and zip_longest() Functions in Python
# TIMESTAMP__2024_08_12__123645

from itertools import zip_longest


# Function to demonstrate zip() with dictionaries
def demonstrate_zip(dict1, dict2):
    return list(zip(dict1, dict2))


# Function to demonstrate zip_longest() with dictionaries
def demonstrate_zip_longest(dict1, dict2):
    return list(zip_longest(dict1, dict2))


# Example dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"x": 7, "y": 8}

# Using zip() with dictionaries
zipped = demonstrate_zip(dict1, dict2)
print("Result of zip() with dictionaries:")
print(zipped)

# Using zip_longest() with dictionaries
zipped_longest = demonstrate_zip_longest(dict1, dict2)
print("\nResult of zip_longest() with dictionaries:")
print(zipped_longest)

# Example lists
list1 = [1, 2, 3]
list2 = [4, 5]

# Using zip() with lists
zipped_lists = list(zip(list1, list2))
print("\nResult of zip() with lists:")
print(zipped_lists)

# Using zip_longest() with lists
zipped_longest_lists = list(zip_longest(list1, list2))
print("\nResult of zip_longest() with lists:")
print(zipped_longest_lists)
