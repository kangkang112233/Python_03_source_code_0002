# Understanding Tuples in Python
# TIMESTAMP__2024_08_04__114146
# This example demonstrates the nature of tuples in Python, especially focusing on single-element tuples.

# An empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)
print("Type of empty tuple:", type(empty_tuple))  # Output: <class 'tuple'>

# A single-element tuple requires a comma
single_element_tuple = (1,)
print("\nSingle-element tuple:", single_element_tuple)
print(
    "Type of single-element tuple:", type(single_element_tuple)
)  # Output: <class 'tuple'>

# Without the comma, it's just the value within parentheses
not_a_tuple = 1
print("\nNot a tuple:", not_a_tuple)
print("Type of not a tuple:", type(not_a_tuple))  # Output: <class 'int'>
