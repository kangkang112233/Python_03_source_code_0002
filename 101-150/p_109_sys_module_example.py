# Knowledge Point: Using sys module for input and output

import sys


# Function to demonstrate sys.stdout.write()
def custom_print(message):
    sys.stdout.write(message + "\n")


# Function to demonstrate sys.stdin.read()
def custom_input():
    sys.stdout.write("Please enter some text and press Enter: ")
    return sys.stdin.read().strip()  # Use strip to remove trailing newline


# Example usage in a library management system

# Using custom_print to output a message
custom_print("Welcome to the Library Management System")

# Using custom_input to get user input
user_input = custom_input()
custom_print(f"You entered: {user_input}")

# Further processing of user_input can be done here
