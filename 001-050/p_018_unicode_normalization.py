# `unicodedata.normalize` を使用したUnicode正規化: `normalize` メソッドは、異なるUnicode文字を正規化し、一貫性のある表現を提供します。
# 例として、`unicodedata.normalize('NFC', 'Spa\u0301m')` は、組み合わせ文字 `a\u0301`（アクセント付き文字）を単一の文字 `á` に正規化し、
# 結果として `Spám` を返します。
#
# Unicode Normalization with `unicodedata.normalize`: The `normalize` method provides a consistent representation
# of different Unicode characters by normalizing them.
# For example, `unicodedata.normalize('NFC', 'Spa\u0301m')` normalizes the combining character `a\u0301`
# (accented character) to a single character `á`, resulting in `Spám`.

import unicodedata

# Normalize the string using NFC normalization form
normalized_text = unicodedata.normalize("NFC", "Spa\u0301m")

# Print the normalized text
print(normalized_text)  # Outputs: Spám

# Example: Book Management System - Normalize book titles

# Sample book title with combining character
book_title = "Sánn\u0301chez"

# Normalize the book title
normalized_title = unicodedata.normalize("NFC", book_title)

# Print the normalized book title
print(normalized_title)  # Outputs: Sánchez

# Explanation:
# In the example above, the book title contains a combining character `á` represented as `a\u0301`.
# The `unicodedata.normalize('NFC', book_title)` function call normalizes the title, resulting in `Sánchez`.
