# Explanation of yield Statement and next() Function in Python
# TIMESTAMP__2024_08_12__162819


def simple_generator():
    yield 1
    yield 2
    yield 3


# Create generator object
gen = simple_generator()

# Retrieve values using next()
print("First value:", next(gen))
print("Second value:", next(gen))
print("Third value:", next(gen))

# Using for loop to retrieve values from generator
for value in simple_generator():
    print("Value from for loop:", value)
