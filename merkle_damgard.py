from utils import pad_message

def merkle_damgard(message: bytes, block_size: int, compression_func):
    """
    Generic Merkle–Damgård construction.
    """
    padded = pad_message(message, block_size)
    blocks = [
        padded[i:i + block_size]
        for i in range(0, len(padded), block_size)
    ]

    chaining_value = b'\x00' * 32  # IV for SHA-256 (256 bits)

    for block in blocks:
        chaining_value = compression_func(block, chaining_value)

    return chaining_value
