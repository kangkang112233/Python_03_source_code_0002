# `try-except` 構文の正しい順序: `try` ブロックから始めて、次に `except`、必要に応じて `else`、
# そして `finally` ブロックが続きます。この順序はエラーハンドリングとクリーンアップ処理を効果的に行うために必要です。
# `finally` ブロックは常に最後に実行されます。
#
# Correct order of `try-except` structure: Start with a `try` block,
# followed by `except`, optionally `else`, and finally a `finally` block.
# This order is essential for effective error handling and cleanup.
# The `finally` block always executes last.

# Example: Book Management System


def get_book_info(book_id, book_database):
    try:
        print("Trying to access the database...")  # Indicate try block execution
        # Try to get the book information
        book = book_database[book_id]
    except KeyError:
        print("An error occurred.")  # Indicate except block execution
        # Handle the error if the book_id is not found
        return f"Book with ID {book_id} not found."
    else:
        print("Successfully accessed the database.")  # Indicate else block execution
        # Execute this block if no exception was raised
        return f"Title: {book['title']}\nAuthor: {book['author']}\nCopies: {book['copies']}\n"
    finally:
        print("Database access attempted.")  # This block will always be executed


# Sample book database
book_database = {
    1: {"title": "1984", "author": "George Orwell", "copies": 5},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 3},
}

# Get book information
print(get_book_info(1, book_database))  # Existing book
print(get_book_info(3, book_database))  # Non-existing book
