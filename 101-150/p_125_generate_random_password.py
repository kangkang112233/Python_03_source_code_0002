# Generating Random Passwords Using `secrets` Module
# TIMESTAMP__2024_08_03__143803
# This example demonstrates how to generate a random password in a library management system.

import secrets
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for i in range(length))
    return password


# Generate a random password
random_password = generate_password()
print("Generated random password:", random_password)
