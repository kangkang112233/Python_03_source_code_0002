from operator import itemgetter

# 図書のリスト (辞書のリスト)
books = [
    {"title": "Book A", "author": "Author X", "year": 2001},
    {"title": "Book B", "author": "Author Y", "year": 1999},
    {"title": "Book C", "author": "Author X", "year": 2005},
    {"title": "Book D", "author": "Author Z", "year": 2010},
]

# 著者名でソート
sorted_books_by_author = sorted(books, key=itemgetter("author"))
print("Books sorted by author:")
for book in sorted_books_by_author:
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

print("\n")

# 発行年でソート
sorted_books_by_year = sorted(books, key=itemgetter("year"))
print("Books sorted by year:")
for book in sorted_books_by_year:
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
