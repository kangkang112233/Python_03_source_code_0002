# Handling TypeError: Unsupported Operand Type(s) for +: 'NoneType' and 'int'
# TIMESTAMP__2024_08_04__170438
# This example demonstrates how to handle TypeError in a library management system.


def add(a, b):
    """
    Adds two numbers, ensuring neither is None.

    Args:
        a (int or None): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b, treating None as 0.
    """
    if a is None:
        a = 0
    return a + b


# Examples
try:
    result = add(None, 5)
    print("Result:", result)  # Output: 5

    result = add(3, 5)
    print("Result:", result)  # Output: 8

    result = add(None, None)
    print("Result:", result)
except TypeError as e:
    print("Error:", e)
