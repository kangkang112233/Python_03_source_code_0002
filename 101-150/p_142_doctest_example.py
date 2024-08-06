# Using doctest in Python
# TIMESTAMP__2024_08_04__165810
# This example demonstrates how to use doctest in a library management system.


def add(a, b):
    """
    Adds two numbers and returns the result.

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
