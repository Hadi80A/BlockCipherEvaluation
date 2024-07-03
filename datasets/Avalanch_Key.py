import sys
import os
import secrets
import random
from baby_rijndael import babyr_enc

sys.path.append(os.getcwd())


def encrypt(plaintext, key):
    # Replace this function with the actual encryption function
    return babyr_enc(plaintext, key)


def generate_random_key(block_size=16):
    # Use the secrets module for secure random key generation
    return secrets.randbits(block_size)


def avalanche_key_dataset(encryption_function=encrypt, num_samples=1000, block_size=16):
    """
    Generate a dataset for avalanche testing with varying keys.

    Args:
    - encryption_function: The encryption function to test.
    - num_samples: Number of samples to generate.
    - block_size: Size of the encryption block.

    Returns:
    A list of dictionaries, each containing information about a sample.
    """
    dataset = []

    for _ in range(num_samples):
        # Generate a random plaintext
        plaintext = random.randint(0, 2 ** block_size - 1)

        # Generate two slightly different keys
        original_key = generate_random_key(block_size)
        modified_key = original_key ^ (1 << random.randint(0, block_size - 1))

        # Encrypt with the original key
        original_ciphertext = encrypt(plaintext, original_key)

        # Encrypt with the modified key
        modified_ciphertext = encrypt(plaintext, modified_key)

        # Record the sample in the dataset
        dataset.append({
            'plaintext': plaintext,
            'original_key': original_key,
            'modified_key': modified_key,
            'original_ciphertext': original_ciphertext,
            'modified_ciphertext': modified_ciphertext,
        })

    return dataset
