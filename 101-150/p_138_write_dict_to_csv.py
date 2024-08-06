# Writing Dictionary Data to a CSV File Using `DictWriter`
# TIMESTAMP__2024_08_04__154008
# This example demonstrates how to write dictionary data to a CSV file using DictWriter in a library management system.

import csv

# Sample dictionary data
data = [
    {"title": "Python Programming", "author": "John Doe", "year": 2021},
    {"title": "Learning Python", "author": "Jane Doe", "year": 2019},
    {"title": "Effective Python", "author": "Brett Slatkin", "year": 2015},
]

# Define the CSV file field names
fieldnames = ["title", "author", "year"]

# Write the dictionary data to a CSV file
with open("books.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Dictionary data written to books.csv")
