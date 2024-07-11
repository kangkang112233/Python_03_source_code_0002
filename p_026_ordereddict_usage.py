# Import necessary module
from collections import OrderedDict

# Create an OrderedDict to track borrowed books
borrowed_books = OrderedDict()


# Function to borrow a book
def borrow_book(book_title):
    borrowed_books[book_title] = borrowed_books.get(book_title, 0) + 1
    borrowed_books.move_to_end(
        book_title
    )  # Move the book to the end to indicate it was recently borrowed


# Function to return the most recently borrowed book
def return_most_recent_book():
    if borrowed_books:
        return borrowed_books.popitem(
            last=True
        )  # Remove and return the last item (most recently borrowed)
    else:
        return None


# Borrow some books
borrow_book("The Catcher in the Rye")
borrow_book("1984")
borrow_book("To Kill a Mockingbird")
borrow_book("The Great Gatsby")
borrow_book("1984")  # Borrowing "1984" again

# Print the current state of borrowed books
print("Current borrowed books (most recent last):")
for book, count in borrowed_books.items():
    print(f"{book}: {count} times")

# Return the most recently borrowed book
most_recent_book = return_most_recent_book()
print("\nMost recently borrowed book returned:")
print(most_recent_book)

# Print the state of borrowed books after returning the most recent one
print("\nBorrowed books after returning the most recent one:")
for book, count in borrowed_books.items():
    print(f"{book}: {count} times")
