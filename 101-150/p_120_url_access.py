# Accessing URL with urlopen
# TIMESTAMP__2024_08_03__113538
# This example demonstrates how to access a URL and read data in a library management system.

from urllib.request import urlopen

# URL of the data to be accessed
url = "https://zh.wikipedia.org/zh-cn/%E6%99%82%E9%96%93%E6%88%B3"

# Accessing the URL and reading the data
with urlopen(url) as response:
    data = response.read().decode("utf-8")

print("Data retrieved from URL:\n", data)
