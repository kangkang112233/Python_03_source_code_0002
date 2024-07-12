# Book management system example using generator and converting to list to get size


# Generator function to simulate book data generation
def book_generator():
    # Initial book ID
    book_id = 1
    # Infinite loop to generate books
    while True:
        # Yield a dictionary representing a book
        yield {
            "id": book_id,
            "title": f"Book Title {book_id}",
            "author": f"Author {book_id}",
        }
        # Increment book ID
        book_id += 1


# Function to get a specified number of books from the generator
def get_books(generator, count):
    books = []
    for _ in range(count):
        books.append(next(generator))
    return books


# Function to convert generator to list and get its size
def generator_size(generator_func, count):
    # Create a new generator object
    generator = generator_func()
    books = get_books(generator, count)
    book_list = list(books)
    return len(book_list)


# Example usage
count = 5
size = generator_size(book_generator, count)
print(f"Size of the generator (converted to list) with {count} elements: {size}")

# Create a new generator object for processing
gen = book_generator()
# Process and print book data
books_list = get_books(gen, count)
for book in books_list:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")
