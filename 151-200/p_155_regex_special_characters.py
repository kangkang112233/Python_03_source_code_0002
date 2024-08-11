# Explanation of Special Characters in Regular Expressions
# TIMESTAMP__2024_08_11__113816

import re


# Function to validate book codes using regular expressions
def validate_book_code(book_code: str) -> bool:
    # Book code pattern: 3 letters followed by 4 digits
    pattern = r"^[A-Za-z]{3}\d{4}$"
    return bool(re.match(pattern, book_code))


# Example book codes
valid_code = "ABC1234"
invalid_code = "A1C1234"

# Validating book codes
print(f"Is '{valid_code}' a valid book code? {validate_book_code(valid_code)}")
print(f"Is '{invalid_code}' a valid book code? {validate_book_code(invalid_code)}")
