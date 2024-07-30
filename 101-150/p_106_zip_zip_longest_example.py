# Knowledge Point: zip() and zip_longest() functions

from itertools import zip_longest

# Lists of book titles and authors with different lengths
book_titles = ["Book A", "Book B", "Book C"]
book_authors = ["Author 1", "Author 2"]

# Using zip() to pair titles and authors based on the shorter length
paired_books_zip = list(zip(book_titles, book_authors))
print("Using zip():")
for title, author in paired_books_zip:
    print(f"Title: {title}, Author: {author}")

# Using zip_longest() to pair titles and authors based on the longer length, with fillvalue set to 'Unknown'
paired_books_zip_longest = list(
    zip_longest(book_titles, book_authors, fillvalue="Unknown")
)
print("\nUsing zip_longest():")
for title, author in paired_books_zip_longest:
    print(f"Title: {title}, Author: {author}")
