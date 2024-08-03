# Parsing Query Strings
# TIMESTAMP__2024_08_03__112258
# This example demonstrates the use of `parse_qs` and `parse_qsl` in a library management system.

from urllib.parse import parse_qs, parse_qsl

# Sample query string representing book search parameters
query_string = "title=Python+Programming&author=John+Doe&year=2021&year=2022"

# Using parse_qs to parse query string into a dictionary
parsed_qs = parse_qs(query_string)
print("Result of parse_qs:\n", parsed_qs)

# Using parse_qsl to parse query string into a list of tuples
parsed_qsl = parse_qsl(query_string)
print("\nResult of parse_qsl:\n", parsed_qsl)
