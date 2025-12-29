"""
Demonstrates the length extension vulnerability
of Merkle–Damgård-based hash functions.
"""

from merkle_damgard import merkle_damgard
from compression import sha256_compression

BLOCK_SIZE = 64

original_message = b"user=omar&role=user"
append_data = b"&role=admin"

original_hash = merkle_damgard(
    original_message,
    BLOCK_SIZE,
    sha256_compression
)

forged_message = original_message + append_data
forged_hash = merkle_damgard(
    forged_message,
    BLOCK_SIZE,
    sha256_compression
)

print("Original Hash:", original_hash.hex())
print("Forged Hash:  ", forged_hash.hex())
print("\n⚠ This demonstrates why raw hash constructions should NOT be used for authentication.")
