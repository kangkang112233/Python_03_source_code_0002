# Alternative example demonstrating the use of TypeVar in type hints

from typing import TypeVar, Generic, List

# Defining the generic type variable
ItemType = TypeVar("ItemType")


class Library(Generic[ItemType]):
    def __init__(self):
        self.items: List[ItemType] = []

    def add_item(self, item: ItemType) -> None:
        self.items.append(item)
        print(f"Item added: {item}")

    def get_items(self) -> List[ItemType]:
        return self.items


# Book class
class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __repr__(self) -> str:
        return f"Book[ID: {self.book_id}, Title: {self.title}, Author: {self.author}]"


# DVD class
class DVD:
    def __init__(self, dvd_id: int, title: str, director: str):
        self.dvd_id = dvd_id
        self.title = title
        self.director = director

    def __repr__(self) -> str:
        return f"DVD[ID: {self.dvd_id}, Title: {self.title}, Director: {self.director}]"


# Creating a library for books
book_library = Library[Book]()
book1 = Book(1, "1984", "George Orwell")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
book_library.add_item(book1)
book_library.add_item(book2)
print("\nBooks in library:")
print(book_library.get_items())

# Creating a library for DVDs
dvd_library = Library[DVD]()
dvd1 = DVD(1, "Inception", "Christopher Nolan")
dvd2 = DVD(2, "The Matrix", "Wachowskis")
dvd_library.add_item(dvd1)
dvd_library.add_item(dvd2)
print("\nDVDs in library:")
print(dvd_library.get_items())
