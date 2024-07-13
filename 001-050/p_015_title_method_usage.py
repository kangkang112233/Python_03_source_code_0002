# Pythonでの `title` メソッドの使用: `title` メソッドは文字列の各単語の最初の文字を大文字に変換し、他の文字を小文字にします。
# 例えば、`"hello world".title()` は `"Hello World"` を返します。タイトルや書籍名のフォーマットに便利です。
#
# Using `title` Method in Python: The `title` method in Python converts the first character of each word in a string
# to uppercase and all other characters to lowercase. For example, `"hello world".title()` returns `"Hello World"`.
# It is useful for formatting titles or book names.

# Example: Book Management System - Format book titles

# Sample book title
book_title = "the great gatsby"

# Use title method to format the book title
formatted_title = book_title.title()

# Print the formatted title
print(formatted_title)  # Outputs: The Great Gatsby

# Example with user input
user_input = "to kill a mockingbird"

# Format the user input using title method
formatted_input = user_input.title()

# Print the formatted user input
print(formatted_input)  # Outputs: To Kill A Mockingbird
