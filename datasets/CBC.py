import sys
import os
import random
from baby_rijndael import babyr_enc, babyr_dec

sys.path.append(os.getcwd())


def convert_bytes_list_to_hex_integer(bytes_list: list) -> int:
    """
    Convert a list of bytes to a hexadecimal integer.

    Args:
    - bytes_list: The list of bytes to convert.

    Returns:
    An integer representing the hexadecimal value of the byte list.
    """
    hex_representation = ''.join([hex(x)[2:].zfill(2) for x in bytes_list])

    # Convert the concatenated hexadecimal string to an integer
    return int(hex_representation, 16)


def generate_cbc_dataset(size):
    """
    Generate a dataset for Cipher Block Chaining (CBC) mode.

    Args:
    - size: Number of pairs to generate.

    Returns:
    A list of tuples, each containing a ciphertext and key pair.
    """
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext and key
        plaintext = random.randint(0, 0xFFFF)
        key = random.randint(0, 0xFFFF)

        # Generate a random 16-bit Initialization Vector (IV)
        initialization_vector = random.randint(0, 0xFFFF)

        # Encrypt the plaintext using CBC mode
        ciphertext = initialization_vector  # Initialization Vector for the first block
        for i in range(16):
            # XOR the plaintext with the previous ciphertext (or IV for the first block)
            plaintext ^= ciphertext
            # Encrypt the XORed result
            ciphertext = convert_bytes_list_to_hex_integer(babyr_enc(plaintext, key))

            # Append the encrypted block to the dataset
            dataset.append((ciphertext, key))

    return dataset

