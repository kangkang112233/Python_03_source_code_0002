import timeit


# Example for a library management system
# Function to add a book to a library
def add_book_to_library(library, title, author):
    book = {"title": title, "author": author}
    library.append(book)


# Wrapper function to initialize the library and add a book
def wrapper():
    library = []
    add_book_to_library(library, "1984", "George Orwell")


# Measure the time using timeit.repeat()
# By default, it repeats the timeit() 5 times
execution_times = timeit.repeat(wrapper, repeat=5, number=1000000)

# Output the execution times
for i, exec_time in enumerate(execution_times, start=1):
    print(f"Execution time for run {i}: {exec_time} seconds")

# Output format adjusted for readability
# Execution time for run 1: <execution_time> seconds
# Execution time for run 2: <execution_time> seconds
# Execution time for run 3: <execution_time> seconds
# Execution time for run 4: <execution_time> seconds
# Execution time for run 5: <execution_time> seconds
