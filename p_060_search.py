import re

# Search for pattern 'a.c' in the string 'abcde'
result = re.search("a.c", "abcde")
if result:
    print(f"Pattern found: {result.group()} at position {result.span()}")
else:
    print("Pattern not found")

# Match pattern 'a.c' at the start of the string 'abcde'
result = re.match("a.c", "abcde")
if result:
    print(f"Pattern found: {result.group()} at position {result.span()}")
else:
    print("Pattern not found")

# Search for pattern '.c' in the string 'abcde'
result = re.search(".c", "abcde")
if result:
    print(f"Pattern found: {result.group()} at position {result.span()}")
else:
    print("Pattern not found")

# Match pattern '.c' at the start of the string 'abcde'
result = re.match(".c", "abcde")
if result:
    print(f"Pattern found: {result.group()} at position {result.span()}")
else:
    print("Pattern not found")
