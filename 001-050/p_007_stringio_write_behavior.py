# `io.StringIO` の書き込み動作: `StringIO` オブジェクトを使って文字列をメモリ上で操作します。
# `write` メソッドを使うと、既存の内容が上書きされます。コードの結果は "Hello, world!\nBye!" ではなく "\nBye!" になります。
#
# `io.StringIO` Write Behavior: Using a `StringIO` object to manipulate strings in memory.
# The `write` method overwrites existing content.
# The result of the code is "\nBye!" instead of "Hello, world!\nBye!".

import io


def book_management():
    # Simulate a book entry process using StringIO
    with io.StringIO("Title: 1984\nAuthor: George Orwell") as stream:
        # Writing new content, which overwrites the existing content
        stream.write("\nAvailable Copies: 5")
        result = stream.getvalue()
        print(result)


book_management()
