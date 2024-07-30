# Knowledge Point: Accessing environment variables

import os

# Example function to print the PATH environment variable using different methods


def print_path_variable():
    try:
        path_value = os.environ["PATH"]
        print("Using os.environ['PATH']:")
        print(f"PATH: {path_value}")
    except KeyError:
        print("Environment variable 'PATH' not found using os.environ['PATH']")

    path_value = os.getenv("PATH")
    print("\nUsing os.getenv('PATH'):")
    print(f"PATH: {path_value}")

    path_value = os.environ.get("PATH")
    print("\nUsing os.environ.get('PATH'):")
    print(f"PATH: {path_value}")


# Example usage
print_path_variable()
