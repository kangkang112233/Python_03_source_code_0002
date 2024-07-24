# This code example demonstrates the usage of zip() and zip_longest()
# in the context of a library management system.

from itertools import zip_longest


def pair_books_and_authors(books, authors):
    """
    Pair books and authors using zip and zip_longest.

    Args:
    books (list): A list of book titles.
    authors (list): A list of author names.

    Returns:
    tuple: Two lists of paired book titles and authors.
    """
    paired_using_zip = list(zip(books, authors))  # Pair using zip
    paired_using_zip_longest = list(
        zip_longest(books, authors, fillvalue="Unknown")
    )  # Pair using zip_longest

    return paired_using_zip, paired_using_zip_longest


# Test cases
books = ["Learning Python", "Mastering Data Science", "Introduction to AI"]
authors = ["Mark Lutz", "John Smith"]

# Pair books and authors
paired_zip, paired_zip_longest = pair_books_and_authors(books, authors)

# Display results
print("Paired using zip():")
for pair in paired_zip:
    print(pair)

print("\nPaired using zip_longest():")
for pair in paired_zip_longest:
    print(pair)
