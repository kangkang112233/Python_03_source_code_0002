# Explanation of Retrieving Environment Variable PATH in Python
# TIMESTAMP__2024_08_12__124010

import os


# Retrieve PATH using os.environ['PATH']
def get_path_environ():
    try:
        return os.environ["PATH"]
    except KeyError:
        return "PATH environment variable not found."


# Retrieve PATH using os.getenv('PATH')
def get_path_getenv():
    return os.getenv("PATH", "PATH environment variable not found.")


# Retrieve PATH using os.environ.get('PATH')
def get_path_environ_get():
    return os.environ.get("PATH", "PATH environment variable not found.")


# Print the PATH using different methods
print("Using os.environ['PATH']:")
print(get_path_environ())

print("\nUsing os.getenv('PATH'):")
print(get_path_getenv())

print("\nUsing os.environ.get('PATH'):")
print(get_path_environ_get())
