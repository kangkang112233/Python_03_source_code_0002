import hashlib


# Example for a library management system
# Function to generate the hash of a book's title and author
def generate_book_hash(title, author):
    # Combine title and author into a single string
    data = f"{title}:{author}"
    # Generate SHA-256 hash
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()


# Function to verify the integrity of a book's data using its hash
def verify_book_hash(title, author, expected_hash):
    # Generate the hash for the provided title and author
    calculated_hash = generate_book_hash(title, author)
    # Compare the calculated hash with the expected hash
    return calculated_hash == expected_hash


# Example usage
title = "1984"
author = "George Orwell"
# Generate the hash for the book
book_hash = generate_book_hash(title, author)
print(f"Hash for the book '{title}' by {author}: {book_hash}")

# Verify the hash
is_valid = verify_book_hash(title, author, book_hash)
print(f"Is the hash valid? {'Yes' if is_valid else 'No'}")

# Output:
# Hash for the book '1984' by George Orwell: <generated_hash_value>
# Is the hash valid? Yes
