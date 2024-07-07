# 辞書のアンパック: 辞書のキー、値、またはすべての要素を変数にアンパックする方法。
# 辞書のキーをアンパックするには、辞書を直接アンパックし、
# 値をアンパックするには `.values()` を使用し、すべての要素をアンパックするには `.items()` を使用します。
#
# Dictionary Unpacking: How to unpack dictionary keys, values, or all elements into variables.
# To unpack dictionary keys, unpack the dictionary directly.
# To unpack values, use `.values()`. To unpack all elements, use `.items()`.

# Example: Book Management System

# Define a dictionary with book information
book_info = {"title": "1984", "author": "George Orwell", "copies": 5}

# Unpacking keys
title_key, author_key, copies_key = book_info
print(f"Keys: {title_key}, {author_key}, {copies_key}\n")

# Unpacking values
title, author, copies = book_info.values()
print(f"Title: {title}\nAuthor: {author}\nCopies: {copies}\n")

# Unpacking all items
title_item, author_item, copies_item = book_info.items()
print(
    f"Title Item: {title_item}\nAuthor Item: {author_item}\nCopies Item: {copies_item}\n"
)
