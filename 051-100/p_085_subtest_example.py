import unittest


# Function to demonstrate usage of subTest in a library management system
def is_valid_isbn(isbn):
    """
    Validates if the given ISBN number is valid.
    """
    return len(isbn) == 13 and isbn.isdigit()


class TestLibraryMethods(unittest.TestCase):
    def test_is_valid_isbn(self):
        """
        Test the is_valid_isbn function with multiple ISBN numbers.
        """
        test_cases = {
            "9783161484100": True,
            "978316148410": False,
            "97831614841001": False,
            "abcdefghijklm": False,
        }

        for isbn, expected in test_cases.items():
            with self.subTest(isbn=isbn):
                self.assertEqual(is_valid_isbn(isbn), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
