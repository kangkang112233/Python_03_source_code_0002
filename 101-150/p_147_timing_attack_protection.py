# Timing Attacks
# TIMESTAMP__2024_08_04__172353
# This example demonstrates how to protect against timing attacks using hmac.compare_digest in a library management system.

import hmac


# Function to securely compare tokens
def compare_tokens(token1, token2):
    return hmac.compare_digest(token1, token2)


# Example tokens
expected_token = "secure_expected_token"
received_token = "received_token_example"

# Securely compare the tokens
tokens_match = compare_tokens(expected_token, received_token)
print(f"Tokens match: {tokens_match}")
