# Explanation of MagicMock Methods assert_called_once and assert_called_with in Python
# TIMESTAMP__2024_08_12__131512

from unittest.mock import MagicMock


# Example function that uses a mock
def example_function(mock):
    mock("hello", key="value")


# Creating a MagicMock object
mock = MagicMock()

# Calling the example function with the mock
example_function(mock)
example_function(mock)

# Asserting that the mock was called exactly once
try:
    mock.assert_called_once()
    print("Mock was called exactly once.")
except AssertionError:
    print("Mock was not called exactly once.")

# Asserting that the mock was called with specific arguments
try:
    mock.assert_called_with("hello", key="value")
    print("Mock was called with the correct arguments.")
except AssertionError:
    print("Mock was not called with the correct arguments.")
