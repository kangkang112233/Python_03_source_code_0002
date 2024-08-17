# Explanation of group() Method in Python's re Module
# TIMESTAMP__2024_08_13__101056

import re

# Sample text
text = "The rain in Spain"

# Compile a regular expression pattern
pattern = re.compile(r"(rain) in (Spain)")

# Search for the pattern in the text
match = pattern.search(text)

if match:
    print("Full match:", match.group(0))  # Entire match
    print("First group:", match.group(1))  # First capture group
    print("Second group:", match.group(2))  # Second capture group
    print(
        "Second character of full match:", match.group(0)[1]
    )  # Second character of the entire match

    # Usage examples for match[1] and match[0]
    print("First group using index:", match[1])  # Equivalent to match.group(1)
    print("Full match using index:", match[0])  # Equivalent to match.group(0)
