# Using the `yield` Statement to Create Generator Objects
# TIMESTAMP__2024_08_04__111940
# This example demonstrates how to use the `yield` statement in a library management system.


def generate_book_ids():
    book_id = 1
    while book_id <= 5:
        yield book_id
        book_id += 1


# Using a for loop to get values from the generator
print("Book IDs using for loop:")
for book_id in generate_book_ids():
    print(book_id)

# Using next() to get values from the generator
print("\nBook IDs using next():")
book_ids = generate_book_ids()
print(next(book_ids))  # Output: 1
print(next(book_ids))  # Output: 2
print(next(book_ids))  # Output: 3
print(next(book_ids))  # Output: 4
print(next(book_ids))  # Output: 5
