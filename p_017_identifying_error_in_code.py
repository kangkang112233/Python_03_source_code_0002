# エラーの発生するコードを特定する: `"Hello 🌍!"` は文字列（str）であり、文字列には `search` メソッドは存在しません。
# `search` メソッドは正規表現を使用する場合に `re` モジュールで提供されます。このコードは `AttributeError` を発生させます。
#
# Identifying Error in Code: `"Hello 🌍!"` is a string, and strings do not have a `search` method.
# The `search` method is available in the `re` module when working with regular expressions.
# This code will raise an `AttributeError`.

# Example: Incorrect usage of search method

# This code will raise an AttributeError because 'str' object has no attribute 'search'
try:
    result = "Hello 🌍!".search("🌍")
except AttributeError as e:
    print(e)  # Outputs: 'str' object has no attribute 'search'

# Correct usage of search method with re module
import re

# Correctly use re.search to find a pattern in a string
match = re.search("🌍", "Hello 🌍!")
if match:
    print(f"Found: {match.group(0)}")
else:
    print("Not found")

# Example: Book Management System - Search for book titles with a keyword

# List of book titles
book_titles = ["1984", "To Kill a Mockingbird", "The Great Gatsby"]


# Function to search for a keyword in book titles
def search_books(keyword, titles):
    return [title for title in titles if re.search(keyword, title, re.IGNORECASE)]


# Search for books containing the keyword "great"
search_result = search_books("great", book_titles)

# Print the search result
print("Search Results:", search_result)
# Outputs: Search Results: ['The Great Gatsby']
