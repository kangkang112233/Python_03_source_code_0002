# `.join` メソッドの使用: `join` メソッドは、イテラブルなオブジェクトの各要素を特定の文字列で結合するために使用されます。
# 文字列のリストやタプルを結合する際に便利です。例えば、`" ".join("abc")` は `a b c` を返し、`"-".join(["1", "2", "3"])` は `1-2-3` を返します。
#
# Using `.join` Method: The `join` method is used to concatenate each element of an iterable object with a specified string.
# It is useful for joining lists or tuples of strings. For example, `" ".join("abc")` returns `a b c`, and `"-".join(["1", "2", "3"])` returns `1-2-3`.

# Example: Book Management System - Display book details with formatted strings

# List of book attributes
book_attributes = ["Title: 1984", "Author: George Orwell", "Copies: 5"]

# Use join to create a single string with each attribute on a new line
formatted_book_details = "\n".join(book_attributes)

# Print the formatted book details
print(formatted_book_details)
# Outputs:
# Title: 1984
# Author: George Orwell
# Copies: 5

# Example with given text
target = "any text"
print(" ".join(target))  # Outputs: a n y   t e x t
