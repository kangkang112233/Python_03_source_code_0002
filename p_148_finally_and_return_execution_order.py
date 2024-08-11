# Knowledge point: Execution Order of finally and return
# TIMESTAMP__2024_08_06__223817


def example_function():
    try:
        print("Inside try block")
        return "Return from try block"
    finally:
        print("Inside finally block")
        # Uncomment the next line to see how it affects the return value
        # return "Return from finally block"


result = example_function()
print(f"Result: {result}")

# In this example:
# - "Inside try block" will be printed first.
# - "Inside finally block" will be printed next.
# - Finally, the return value from the try block will be printed.
# If the return statement in the finally block is uncommented,
# it will override the return value from the try block.
