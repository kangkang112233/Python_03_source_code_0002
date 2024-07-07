# `try-except` 構文の正しい順序: `try` ブロックから始めて、次に `except`、必要に応じて `else`、そして `finally` ブロックが続きます。
# この順序はエラーハンドリングとクリーンアップ処理を効果的に行うために必要です。
#
# Correct order of `try-except` structure: Start with a `try` block,
# followed by `except`, optionally `else`, and finally a `finally` block.
# This order is essential for effective error handling and cleanup.

# Example: Book Management System


def get_book_info(book_id, book_database):
    try:
        # Try to get the book information
        book = book_database[book_id]
    except KeyError:
        # Handle the error if the book_id is not found
        return f"Book with ID {book_id} not found."
    else:
        # Execute this block if no exception was raised
        return f"Title: {book['title']}\nAuthor: {book['author']}\nCopies: {book['copies']}\n"
    finally:
        # This block will always be executed
        print("Database access attempted.")


# Sample book database
book_database = {
    1: {"title": "1984", "author": "George Orwell", "copies": 5},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 3},
}

# Get book information
print(get_book_info(1, book_database))  # Existing book
print(get_book_info(3, book_database))  # Non-existing book
