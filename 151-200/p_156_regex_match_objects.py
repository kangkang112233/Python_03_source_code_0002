# Explanation of Match Objects in Regular Expressions
# TIMESTAMP__2024_08_11__115124

import re


# Function to extract book information from a string using regular expressions
def extract_book_info(book_info: str):
    # Pattern to match book title and author
    pattern = r"(?P<title>.+?) by (?P<author>.+)"
    match = re.match(pattern, book_info)
    if match:
        title = match.group(1)
        author = match.group(2)
        return title, author
    else:
        return None


# Example book info strings
book_info_1 = "Python Programming by John Doe"
book_info_2 = "Data Science with Python by Jane Smith"

# Extracting book information
title_1, author_1 = extract_book_info(book_info_1)
title_2, author_2 = extract_book_info(book_info_2)

# Printing extracted information
print(f"Title: {title_1}, Author: {author_1}")
print(f"Title: {title_2}, Author: {author_2}")
# Japanese
# この正規表現(?P<title>.+?) by (?P<author>.+)は、2つの部分に分かれています。(?P<title>.+?)は本のタイトルを、(?P<author>.+)は著者の名前をキャプチャします。

# (?P<title>.+?)：titleという名前のキャプチャグループを作成し、最短一致で任意の文字を0回以上マッチさせます。
# by：文字列"by"をマッチさせます。
# (?P<author>.+)：authorという名前のキャプチャグループを作成し、任意の文字を1回以上マッチさせます。
# Chinese
# 这个正则表达式(?P<title>.+?) by (?P<author>.+)分为两个部分。(?P<title>.+?)捕获书名，(?P<author>.+)捕获作者名字。

# (?P<title>.+?)：创建一个名为title的捕获组，最短匹配任意字符0次或多次。
# by：匹配字符串"by"。
# (?P<author>.+)：创建一个名为author的捕获组，匹配任意字符1次或多次。
# English
# The regular expression (?P<title>.+?) by (?P<author>.+) is divided into two parts. (?P<title>.+?) captures the book title, and (?P<author>.+) captures the author's name.

# (?P<title>.+?): Creates a capturing group named title, matching any character (.) one or more times (.+?), using a non-greedy match (.+?).
# by: Matches the literal string "by".
# (?P<author>.+): Creates a capturing group named author, matching any character (.) one or more times (.+).
