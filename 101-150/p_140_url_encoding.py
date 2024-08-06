# URL Encoding in Python
# TIMESTAMP__2024_08_04__164313
# This example demonstrates how to use urlencode, quote, and quote_plus in a library management system.

import urllib.parse

# Sample dictionary to encode as query string
params = {"title": "Python Programming", "author": "John Doe"}

# Using urlencode to convert dictionary to query string
query_string = urllib.parse.urlencode(params)
print("Encoded query string using urlencode:", query_string)

# Sample strings to encode
sample_string = "Python Programming Guide"

# Using quote to encode the string
encoded_string_quote = urllib.parse.quote(sample_string)
print("\nEncoded string using quote:", encoded_string_quote)

# Using quote_plus to encode the string
encoded_string_quote_plus = urllib.parse.quote_plus(sample_string)
print("Encoded string using quote_plus:", encoded_string_quote_plus)
