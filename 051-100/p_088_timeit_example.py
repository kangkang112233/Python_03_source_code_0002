import timeit


# Example for a library management system
# Function to add a book to a library
def add_book_to_library(library, title, author):
    book = {"title": title, "author": author}
    library.append(book)


# Function to measure the time it takes to add a book
def measure_add_book():
    library = []

    # Define a wrapper function that includes the library initialization
    def wrapper():
        add_book_to_library(library, "1984", "George Orwell")

    # Using timeit to measure the execution time of the wrapper function
    execution_time = timeit.timeit(wrapper, number=1000000)
    print(f"Average execution time over 1,000,000 runs: {execution_time} seconds")


# Measure the time
measure_add_book()

# Output format adjusted for readability
# Average execution time over 1,000,000 runs: <execution_time> seconds
