# unittestモジュールは、Python標準ライブラリに含まれるユニットテストフレームワークであり、テストケースの作成、実行、および結果の報告を支援します。
# これはJavaのJUnitにインスパイアされたもので、クラスベースのテストケースをサポートしています。unittestを使用することで、個々の関数やメソッドが期待通りに動作することを確認でき、
# テストの自動化や継続的インテグレーションに役立ちます。さらに、テストスイートの作成やテストケースのグループ化、セットアップおよびティアダウンメソッドの実装が可能です。

# The unittest module is a unit testing framework included in the Python standard library that helps in creating, running, and reporting test cases.
# Inspired by Java's JUnit, it supports class-based test cases. Using unittest, you can verify that individual functions and methods work as expected,
# which aids in test automation and continuous integration. Additionally, it allows for creating test suites, grouping test cases, and implementing setup and teardown methods.

import unittest


def add_book(library, book):
    """Add a book to the library."""
    library.append(book)


def remove_book(library, book):
    """Remove a book from the library."""
    if book in library:
        library.remove(book)


class TestLibraryManagement(unittest.TestCase):
    def setUp(self):
        """Set up a fresh library before each test."""
        self.library = []

    def test_add_book(self):
        """Test adding a book to the library."""
        add_book(self.library, "Python Programming")
        self.assertIn("Python Programming", self.library)

    def test_remove_book(self):
        """Test removing a book from the library."""
        add_book(self.library, "Python Programming")
        remove_book(self.library, "Python Programming")
        self.assertNotIn("Python Programming", self.library)

    def tearDown(self):
        """Clean up after each test."""
        self.library = []


if __name__ == "__main__":
    unittest.main()
