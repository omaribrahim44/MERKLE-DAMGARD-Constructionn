import hashlib
from merkle_damgard import merkle_damgard
from compression import sha256_compression

BLOCK_SIZE = 64  # 512 bits = 64 bytes

message = b"This is a test message for Merkle-Damgard construction"

custom_hash = merkle_damgard(message, BLOCK_SIZE, sha256_compression)
standard_hash = hashlib.sha256(message).digest()

print("Custom Merkle–Damgard Hash:", custom_hash.hex())
print("Standard SHA-256 Hash:     ", standard_hash.hex())

assert custom_hash == standard_hash
print("✔ Hash verification successful")
