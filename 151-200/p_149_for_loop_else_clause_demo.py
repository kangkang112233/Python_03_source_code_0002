# Explanation of the else clause in for loops
# TIMESTAMP__2024_08_11__104952


# Function to check if a book is available in the library and print a message accordingly
def check_book_availability(library, book_title):
    for book in library:
        if book["title"] == book_title:
            print(f"Book '{book_title}' is available in the library.")
            break
    else:
        print(f"Book '{book_title}' is not available in the library.")


# Example library list
library = [
    {"title": "Python Programming", "author": "John Doe"},
    {"title": "Data Science with Python", "author": "Jane Smith"},
    {"title": "Machine Learning Basics", "author": "Alan Turing"},
]

# Checking for a book that is in the library
check_book_availability(library, "Data Science with Python")

# Checking for a book that is not in the library
check_book_availability(library, "Deep Learning with Python")
