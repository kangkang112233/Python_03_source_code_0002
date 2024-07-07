# DoctestはPythonの組み込みモジュールで、
# ドキュメントに書かれたテストケースを実行するために使用されます。
# テストは通常、インタープリタセッションのように見え、
# コードと予期される出力のペアで構成されています。

# Doctest is a built-in Python module used to execute test cases
# written in documentation. Tests usually look like an interpreter session,
# consisting of pairs of code and expected output.


def add_book(library, book):
    """
    Adds a book to the library.

    Args:
    library (dict): The library database.
    book (dict): A dictionary containing book information.

    Returns:
    dict: Updated library database.

    Example:
    >>> library = {}
    >>> book = {'title': 'Python 101', 'author': 'John Doe'}
    >>> add_book(library, book)
    {'Python 101': {'title': 'Python 101', 'author': 'John Doe'}}
    """
    library[book["title"]] = book
    return library


def get_book(library, title):
    """
    Retrieves a book from the library by title.

    Args:
    library (dict): The library database.
    title (str): The title of the book to retrieve.

    Returns:
    dict: The book information.

    Example:
    >>> library = {'Python 101': {'title': 'Python 101', 'author': 'John Doe'}}
    >>> get_book(library, 'Python 101')
    {'title': 'Python 101', 'author': 'John Doe'}
    """
    return library.get(title)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
