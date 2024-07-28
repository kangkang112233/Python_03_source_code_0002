import unittest


class TestLibraryMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up resources needed for the entire test class.
        """
        cls.library_db = "LibraryDatabase"  # Simulate a database connection setup
        print("Set up class-level resources.")

    def setUp(self):
        """
        Set up resources needed for each test method.
        """
        self.book_list = ["Book A", "Book B", "Book C"]  # Simulate a fresh book list
        print("Set up test-level resources.")

    def test_add_book(self):
        """
        Test adding a book to the book list.
        """
        self.book_list.append("Book D")
        self.assertIn("Book D", self.book_list)

    def test_remove_book(self):
        """
        Test removing a book from the book list.
        """
        self.book_list.remove("Book B")
        self.assertNotIn("Book B", self.book_list)

    def tearDown(self):
        """
        Clean up resources used in each test method.
        """
        self.book_list = None  # Simulate cleaning up book list
        print("Tear down test-level resources.")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up resources used by the entire test class.
        """
        cls.library_db = None  # Simulate closing database connection
        print("Tear down class-level resources.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
