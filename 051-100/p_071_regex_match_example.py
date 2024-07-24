# This code example demonstrates the usage of re.match and re.search
# in the context of a library management system.

import re


def match_pattern(text, pattern):
    """
    Match the given pattern at the start of the text using re.match,
    and search for the pattern anywhere in the text using re.search.

    Args:
    text (str): The text to be processed.
    pattern (str): The regex pattern to be matched.

    Returns:
    tuple: Results of re.match and re.search.
    """
    match_result = re.match(pattern, text)  # Match pattern from the start of the text
    search_result = re.search(pattern, text)  # Search pattern anywhere in the text
    return match_result, search_result


# Test cases
text = "abcd"
pattern = ".cd"

# Process text
match_result, search_result = match_pattern(text, pattern)
print(f"Match result: {match_result}")
print(f"Search result: {search_result}")
