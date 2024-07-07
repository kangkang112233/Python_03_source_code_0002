# `NameError` 例外の処理: Pythonでは、定義されていない変数を参照すると `NameError` が発生します。
# `try` ブロック内で未定義の変数 `b` を使用しているため、`except NameError` ブロックが実行され、
# 「特定のエラーです」というメッセージが表示されます。
#
# Handling `NameError` Exception: In Python, a `NameError` occurs when a variable that is not defined is referenced.
# Since the `try` block uses an undefined variable `b`, the `except NameError` block is executed,
# displaying the message "特定のエラーです" (This is a specific error).


def func3():
    a = 1
    d = 2

    try:
        # Attempt to print the sum of 'a' and 'b', but 'b' is not defined
        print(a + b)
    except NameError:
        # Handle the NameError exception
        print("特定のエラーです")  # This is a specific error


func3()

# Example: Book Management System - Handling missing book attribute


def get_book_author(book):
    try:
        # Attempt to access the 'author' attribute of the book
        return book["author"]
    except KeyError:
        # Handle the case where the 'author' attribute is not found
        print("特定のエラーです")  # This is a specific error


# Sample book data without 'author' attribute
book = {"title": "1984"}

# Try to get the author of the book
get_book_author(book)
