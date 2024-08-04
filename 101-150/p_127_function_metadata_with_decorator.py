# Function Names and Docstrings with Decorators
# TIMESTAMP__2024_08_04__112626
# This example demonstrates how to preserve function names and docstrings using decorators in a library management system.

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello():
    """Say hello function"""
    print("Hello!")


# Check the function metadata
print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)  # Output: Say hello function

# Call the function
say_hello()
