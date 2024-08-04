# Using doctest
# TIMESTAMP__2024_08_03__114151
# This example demonstrates how to use doctest in a library management system.


def add(a, b):
    """
    Add two numbers and return the result.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

print("Doctests completed.")
