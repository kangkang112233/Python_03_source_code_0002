# Simple decorator example to add logging functionality


# Decorator function to add logging
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result

    return wrapper


# Function to be decorated
@simple_decorator
def multiply(x, y):
    return x * y


# Using the decorated function
result = multiply(3, 4)
print(f"Result: {result}")
