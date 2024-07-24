from urllib.parse import urlparse


# Function to demonstrate URL parsing in a library management system
def parse_library_url(url):
    """
    Parse the given library URL into its components.
    """
    parsed_url = urlparse(url)
    print(f"Scheme: {parsed_url.scheme}")
    print(f"Path: {parsed_url.path}")
    print(f"Query: {parsed_url.query}")
    print(f"Fragment: {parsed_url.fragment}")
    print(f"Hostname: {parsed_url.hostname}")


# Example usage
library_url = "https://www.examplelibrary.com/books?title=python#section2"

# Parse the URL and print its components
parse_library_url(library_url)
