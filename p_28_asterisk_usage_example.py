def manage_books(*books):
    # Print all books in the list
    print("Books in the library:\n" + "\n".join(books))


def update_books(new_book, *existing_books, remove_book):
    # Combine new and existing books, and remove specified book
    updated_books = [new_book] + list(existing_books)
    if remove_book in updated_books:
        updated_books.remove(remove_book)
    return updated_books


# Example usage
books_list = ["Book A", "Book B", "Book C"]
manage_books(*books_list)

new_books = update_books("Book D", *books_list, remove_book="Book B")
print("\nUpdated book list:\n" + "\n".join(new_books))
