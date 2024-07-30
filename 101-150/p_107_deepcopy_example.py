# Knowledge Point: deepcopy() function

import copy

# Example data structure for a library management system
book_catalog = {
    "Book A": {"author": "Author 1", "status": "Available"},
    "Book B": {"author": "Author 2", "status": "Checked Out"},
    "Book C": {"author": "Author 3", "status": "Available"},
}

# Create a deep copy of the book_catalog
backup_catalog = copy.deepcopy(book_catalog)

# Modify the original catalog
book_catalog["Book A"]["status"] = "Checked Out"

# Print both catalogs to show they are independent
print("Original Catalog:")
for book, details in book_catalog.items():
    print(f"Title: {book}, Author: {details['author']}, Status: {details['status']}")

print("\nBackup Catalog:")
for book, details in backup_catalog.items():
    print(f"Title: {book}, Author: {details['author']}, Status: {details['status']}")
