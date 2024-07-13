# 内包表記で辞書型のキーと値を取得: `data.items()` メソッドを使い、辞書のキーと値のペアを取得します。
# リスト内包表記 `[(a, b) for a, b in data.items()]` を使用して、これらのペアをタプルとしてリストに変換します。
#
# List Comprehension for Dictionary Items: Use the `data.items()` method to get key-value pairs from the dictionary.
# The list comprehension `[(a, b) for a, b in data.items()]` converts these pairs into a list of tuples.

# Example: Book Management System

# Sample book data dictionary
book_data = {
    "title": "1984",
    "author": "George Orwell",
    "copies": 5,
    "isbn": "123-456-789",
}

# Convert dictionary items to a list of tuples using list comprehension
book_items = [(key, value) for key, value in book_data.items()]

# Print the list of tuples
print(book_items)
