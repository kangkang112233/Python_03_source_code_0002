# Example for a library management system
# Generator function to simulate reading book titles from a large dataset
def book_title_generator():
    titles = [
        "1984",
        "Brave New World",
        "Fahrenheit 451",
        "The Handmaid's Tale",
        "To Kill a Mockingbird",
    ]
    for title in titles:
        yield title


# Function to demonstrate usage of the generator
def display_titles():
    # Create a generator object
    title_gen = book_title_generator()

    # Use for loop to retrieve values
    print("Using for loop to retrieve book titles:")
    for title in title_gen:
        print(title)

    # Create another generator object since the first one is exhausted
    title_gen = book_title_generator()

    # Use next function to retrieve values
    print("\nUsing next function to retrieve book titles:")
    try:
        while True:
            print(next(title_gen))
    except StopIteration:
        # StopIteration is raised when the generator is exhausted
        print("-------StopIteration is raised when the generator is exhausted")


# Run the function to display titles
display_titles()

# Output:
# Using for loop to retrieve book titles:
# 1984
# Brave New World
# Fahrenheit 451
# The Handmaid's Tale
# To Kill a Mockingbird
#
# Using next function to retrieve book titles:
# 1984
# Brave New World
# Fahrenheit 451
# The Handmaid's Tale
# To Kill a Mockingbird
