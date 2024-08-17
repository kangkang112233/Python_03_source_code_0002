# Explanation of compare_digest Function in Python
# TIMESTAMP__2024_08_13__132239

import hmac
import hashlib

# Sample data
data1 = "Hello, World!"
data2 = "Hello, World!"
data3 = "Hello, Python!"

# Generate digests
digest1 = hashlib.sha256(data1.encode()).digest()
digest2 = hashlib.sha256(data2.encode()).digest()
digest3 = hashlib.sha256(data3.encode()).digest()

# Compare digests
print("digest1 vs digest2:", hmac.compare_digest(digest1, digest2))  # True
print("digest1 vs digest3:", hmac.compare_digest(digest1, digest3))  # False
