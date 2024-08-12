# Explanation of re.I and re.A in Python's re Module
# TIMESTAMP__2024_08_12__120922

import re


# Function to demonstrate re.IGNORECASE
def ignore_case_demo(pattern, text):
    return re.findall(pattern, text, re.IGNORECASE)


# Function to demonstrate re.ASCII
def ascii_demo(pattern, text):
    return re.findall(pattern, text, re.ASCII)


# Example text
text = "Hello World! こんにちは世界! 123"

# Example patterns
pattern_ignore_case = r"hello"
pattern_ascii = r"\w+"

# Demonstrating re.IGNORECASE
print("Ignore case demonstration:")
print(ignore_case_demo(pattern_ignore_case, text))  # Output: ['Hello']

# Demonstrating re.ASCII
print("\nASCII demonstration:")
print(ascii_demo(pattern_ascii, text))  # Output: ['Hello', 'World', '123']
