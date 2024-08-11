# Explanation of Decorators in Python
# TIMESTAMP__2024_08_11__111027

from functools import wraps


# Decorator function to log the activity of book borrowing in a library system
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' completed with result: {result}")
        return result

    return wrapper


# Example function to borrow a book from the library
@log_activity
def borrow_book(library, book_title):
    for book in library:
        if book["title"] == book_title:
            print(f"Borrowing book: {book_title}")
            return True
    print(f"Book '{book_title}' not found in the library.")
    return False


# Example library list
library = [
    {"title": "Python Programming", "author": "John Doe"},
    {"title": "Data Science with Python", "author": "Jane Smith"},
    {"title": "Machine Learning Basics", "author": "Alan Turing"},
]

# Borrowing a book that is available in the library
borrow_book(library, "Data Science with Python")

# Attempting to borrow a book that is not in the library
borrow_book(library, "Deep Learning with Python")
