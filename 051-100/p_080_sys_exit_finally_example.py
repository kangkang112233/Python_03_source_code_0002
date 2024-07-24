# This code example demonstrates the execution of a finally block
# even when sys.exit() is called in the context of a library management system.

import sys


def process_books():
    """
    Process books in the library system.

    Returns:
    None
    """
    try:
        print("Processing books...")
        sys.exit("Exiting the process")
    except SystemExit as e:
        print(f"Caught an exception: {e}")
    finally:
        print("Executing finally block to clean up resources")


# Run the function
process_books()
