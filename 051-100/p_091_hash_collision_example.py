import hashlib


# Function to generate the hash of a book's title and author using SHA-256, MD5, or SHA-1
def generate_book_hash(title, author, algorithm="sha256"):
    data = f"{title}:{author}"
    if algorithm == "sha256":
        hash_object = hashlib.sha256(data.encode())
    elif algorithm == "md5":
        hash_object = hashlib.md5(data.encode())
    elif algorithm == "sha1":
        hash_object = hashlib.sha1(data.encode())
    else:
        raise ValueError("Unsupported hash algorithm")
    return hash_object.hexdigest()


# Example usage to demonstrate hash collision vulnerability
books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "Brave New World", "author": "Aldous Huxley"},
]

# Store hashes in a dictionary for better management
hashes = {"md5": {}, "sha1": {}, "sha256": {}}

# Generate hashes for each book and store them in the dictionary
for book in books:
    title = book["title"]
    author = book["author"]
    hashes["md5"][f"{title} by {author}"] = generate_book_hash(
        title, author, algorithm="md5"
    )
    hashes["sha1"][f"{title} by {author}"] = generate_book_hash(
        title, author, algorithm="sha1"
    )
    hashes["sha256"][f"{title} by {author}"] = generate_book_hash(
        title, author, algorithm="sha256"
    )

# Print the hashes
for algo in hashes:
    print(f"Hashes using {algo.upper()}:")
    for book_info, hash_value in hashes[algo].items():
        print(f"  {book_info}: {hash_value}")


# Check for collisions
def check_collisions(hashes):
    for algo in hashes:
        seen_hashes = set()
        for hash_value in hashes[algo].values():
            if hash_value in seen_hashes:
                return True
            seen_hashes.add(hash_value)
    return False


is_collision = check_collisions(hashes)
print(f"Is there a collision? {'Yes' if is_collision else 'No'}")

# Output:
# Hashes using MD5:
#   1984 by George Orwell: <generated_md5_hash1>
#   Brave New World by Aldous Huxley: <generated_md5_hash2>
# Hashes using SHA1:
#   1984 by George Orwell: <generated_sha1_hash1>
#   Brave New World by Aldous Huxley: <generated_sha1_hash2>
# Hashes using SHA256:
#   1984 by George Orwell: <generated_sha256_hash1>
#   Brave New World by Aldous Huxley: <generated_sha256_hash2>
# Is there a collision? No
