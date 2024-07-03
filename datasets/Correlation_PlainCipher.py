import sys
import os
import random
from baby_rijndael import babyr_enc

sys.path.append(os.getcwd())


def encrypt(plaintext, key):
    """
    Encrypt the given plaintext using a provided key.

    Args:
    - plaintext: The original plaintext to be encrypted.
    - key: The encryption key.

    Returns:
    The resulting ciphertext after encrypting the plaintext with the key.
    """
    return babyr_enc(plaintext, key)


def plaintext_ciphertext_correlation_dataset(encryption_function, num_samples=1000, block_size=16):
    """
    Generate a dataset to analyze the correlation between plaintext and ciphertext.

    Args:
    - encryption_function: The encryption function to use.
    - num_samples: Number of samples to generate.
    - block_size: Size of the encryption block.

    Returns:
    A list of dictionaries, each containing information about a plaintext-ciphertext pair.
    """
    dataset = []
    for _ in range(num_samples):
        # Generate a random plaintext
        plaintext = random.randint(0, 2 ** block_size - 1)

        # Generate a random key
        key = random.randint(0, 2 ** block_size - 1)

        # Encrypt the plaintext with the key
        ciphertext = encrypt(plaintext, key)

        # Record the sample in the dataset
        dataset.append({
            'plaintext': plaintext,
            'key': key,
            'ciphertext': ciphertext,
        })

    return dataset
