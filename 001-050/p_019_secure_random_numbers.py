# セキュリティに特化した乱数生成: `secrets` モジュールは、安全に乱数を生成するために特に設計されており、
# トークンの生成やパスワードリセットリンクなど、セキュリティに関連するタスクに使用されます。
# `secrets` モジュールを使用すると、暗号学的に安全な乱数を生成できます。
#
# Using `secrets` Module for Secure Random Numbers: The `secrets` module is specifically designed to generate secure random numbers
# and is used for security-related tasks such as generating tokens and password reset links.
# The `secrets` module allows generating cryptographically secure random numbers.

import secrets

# Generate a secure token for password reset
reset_token = secrets.token_urlsafe(16)
print(f"Password Reset Token: {reset_token}")

# Example: Book Management System - Generate a secure ID for a new book

# Generate a secure random ID for a new book
book_id = secrets.token_hex(8)
print(f"New Book ID: {book_id}")

# Explanation:
# The `secrets.token_urlsafe` function generates a URL-safe text string suitable for use in URLs.
# The `secrets.token_hex` function generates a random text string in hexadecimal format.
# These functions ensure that the generated values are cryptographically secure.
