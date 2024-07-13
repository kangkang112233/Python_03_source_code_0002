# Book management system example using generator for file reading


# Generator function to read lines from a file
def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


# Function to process book data from file
def process_books(file_path):
    book_gen = read_file_line_by_line(file_path)
    for book in book_gen:
        # Assuming each line in the file represents a book in "ID, Title, Author" format
        book_id, title, author = book.split(", ")
        print(f"ID: {book_id}\nTitle: {title}\nAuthor: {author}\n")


# Example usage
file_path = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-07-04-2230_Python_03_source_code_0002\\0000_test_books.txt"
# The file should contain book data in "ID, Title, Author" format

# Process and print book data
process_books(file_path)
