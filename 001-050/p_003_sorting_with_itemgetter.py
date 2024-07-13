# `itemgetter` を用いたソート: `itemgetter` はオペレータモジュールの関数で、
# 複数の要素を持つタプルやリストをソートするために使用されます。
# 上記のコードでは、リストの各タプルの最初と2番目の要素を基準にソートしています。
# 結果は `[(1, 'a', 2), (1, 'b', 3), (2, 'a', 1)]` になります。
#
# Sorting with `itemgetter`: `itemgetter` is a function from the `operator` module
# used to sort tuples or lists with multiple elements.
# In the given code, it sorts the list based on the first and second elements
# of each tuple. The result is `[(1, 'a', 2), (1, 'b', 3), (2, 'a', 1)]`.

from operator import itemgetter

# Example: Book Management System
# Each tuple represents a book with (shelf_number, author, copies_available)

books = [
    (3, "George Orwell", 5),
    (1, "Haruki Murakami", 2),
    (2, "J.K. Rowling", 10),
    (1, "F. Scott Fitzgerald", 4),
]

# Sort the books by shelf_number and author
sorted_books = sorted(books, key=itemgetter(0, 1))

# Print the sorted list of books
for book in sorted_books:
    print(f"Shelf: {book[0]}\nAuthor: {book[1]}\nCopies Available: {book[2]}\n")
