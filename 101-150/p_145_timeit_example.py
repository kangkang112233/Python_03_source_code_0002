# Using timeit.timeit with globals()
# TIMESTAMP__2024_08_04__171356
# This example demonstrates how to use timeit.timeit with globals() in a library management system.

import timeit


# Sample function to measure
def example_function():
    return sum(range(100000))


# Measure the execution time of example_function
execution_time = timeit.timeit("example_function()", globals=globals(), number=1000)
print(f"Execution time: {execution_time} seconds")
