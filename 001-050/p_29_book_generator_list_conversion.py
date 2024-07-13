# Book management system example using generator and list conversion


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


# Create a generator object
gen = book_generator()


# Function to get a specified number of books from the generator
def get_books(generator, count):
    books = []
    for _ in range(count):
        books.append(next(generator))
    return books


# Function to convert generator to list using list function
def convert_generator_to_list(generator, count):
    books = get_books(generator, count)
    return list(books)


# Get and print 5 books using the generator
books_list = convert_generator_to_list(gen, 5)
for book in books_list:
    print(f"ID: {book['id']}\nTitle: {book['title']}\nAuthor: {book['author']}\n")

# Output example:
# ID: 1
# Title: Book Title 1
# Author: Author 1
#
# ID: 2
# Title: Book Title 2
# Author: Author 2
#
# ID: 3
# Title: Book Title 3
# Author: Author 3
#
# ID: 4
# Title: Book Title 4
# Author: Author 4
#
# ID: 5
# Title: Book Title 5
# Author: Author 5
