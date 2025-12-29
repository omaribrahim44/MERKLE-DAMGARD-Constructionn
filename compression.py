import hashlib

def sha256_compression(block: bytes, chaining_value: bytes) -> bytes:
    """
    SHA-256 used as a compression function.
    """
    sha = hashlib.sha256()
    sha.update(chaining_value + block)
    return sha.digest()
