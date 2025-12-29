def pad_message(message: bytes, block_size: int) -> bytes:
    """
    Merkle–Damgård strengthening padding.
    Appends 0x80, zero padding, and message length (64-bit).
    """
    message_len_bits = len(message) * 8
    message += b'\x80'

    while (len(message) + 8) % block_size != 0:
        message += b'\x00'

    message += message_len_bits.to_bytes(8, byteorder='big')
    return message
