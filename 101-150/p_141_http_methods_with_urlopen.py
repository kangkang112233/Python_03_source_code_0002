# Using urlopen() for HTTP Methods in Python
# TIMESTAMP__2024_08_04__165041
# This example demonstrates how to use urlopen() for different HTTP methods in a library management system.

import urllib.request

# GET request
response = urllib.request.urlopen("http://httpbin.org/get")
print("GET request response:")
print(response.read().decode("utf-8"))

# POST request
data = urllib.parse.urlencode({"name": "John Doe", "age": 28}).encode("utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data)
print("\nPOST request response:")
print(response.read().decode("utf-8"))

# DELETE request
req = urllib.request.Request("http://httpbin.org/delete", method="DELETE")
response = urllib.request.urlopen(req)
print("\nDELETE request response:")
print(response.read().decode("utf-8"))
