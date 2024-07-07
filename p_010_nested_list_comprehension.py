# 条件付きネストされたリスト内包表記: リスト内包表記を使用して、二重ループと条件を組み合わせることができます。
# `[x for x in 'abc' for y in '123' if y == '1']` は、`'abc'` の各文字と `y == '1'` の条件を満たす `y` の組み合わせをリストに追加します。
# この場合、結果は `['a', 'b', 'c']` です。
#
# Nested List Comprehension with Condition: Using list comprehension,
# you can combine nested loops and conditions.
# `[x for x in 'abc' for y in '123' if y == '1']` adds each character from `'abc'`
# for which `y` in `'123'` satisfies `y == '1'` to the list.
# The result is `['a', 'b', 'c']`.

# Example: Book Management System - List of available books for a specific condition

# Sample book data
books = [
    {"title": "1984", "author": "George Orwell", "copies": 5},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 3},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2},
]

# Using list comprehension to filter books with more than 3 copies
available_books = [
    book["title"] for book in books for condition in [book["copies"] > 3] if condition
]

# Print the list of available books
print(available_books)  # Outputs: ['1984']
