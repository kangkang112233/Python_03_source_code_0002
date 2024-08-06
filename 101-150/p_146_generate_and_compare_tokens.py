# Using token_urlsafe() and compare_digest() from secrets module
# TIMESTAMP__2024_08_04__172028
# This example demonstrates how to use token_urlsafe() and compare_digest() in a library management system.

import secrets
import hmac

# Generate a secure token
token = secrets.token_urlsafe(256)
print(f"Generated token: {token}")


# Function to securely compare tokens
def compare_tokens(token1, token2):
    return hmac.compare_digest(token1, token2)


# Example usage
received_token = "received_token_example"
print(f"Tokens match: {compare_tokens(token, received_token)}")
