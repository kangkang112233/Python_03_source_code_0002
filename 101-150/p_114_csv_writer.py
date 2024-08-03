# Knowledge Point: CSV Module Writer

import csv


# Function to demonstrate writing to a CSV file with a custom delimiter
def save_books_to_csv(file_path, books):
    # Open the file in write mode
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        # Create a CSV writer object with a tab delimiter
        writer = csv.writer(file, delimiter="\t")

        # Write the header row
        writer.writerow(["Title", "Author", "Year"])

        # Write each book's data as a new row
        for book in books:
            writer.writerow([book["title"], book["author"], book["year"]])


# Example usage in a library management system
books = [
    {"title": "Book A", "author": "Author 1", "year": 2021},
    {"title": "Book B", "author": "Author 2", "year": 2020},
    {"title": "Book C", "author": "Author 3", "year": 2019},
]

save_books_to_csv("books.csv", books)

print("Books data has been written to 'books.csv' using a tab delimiter.")
