import sys
import os
import random
import secrets
from baby_rijndael import babyr_enc

sys.path.append(os.getcwd())


def generate_random_key(block_size=16):
    # Use the secrets module for secure random key generation
    return secrets.randbits(block_size)


def encrypt(plaintext, key):
    """
    Encrypt the plaintext using a given key.

    Args:
    - plaintext: The original plaintext.
    - key: The encryption key.

    Returns:
    The ciphertext obtained by encrypting the plaintext with the key.
    """
    return babyr_enc(plaintext, key)


def plaintext_avalanche_dataset(encryption_function=encrypt, num_samples=1000, block_size=16):
    """
    Generate a dataset for plaintext avalanche testing.

    Args:
    - encryption_function: The encryption function to test.
    - num_samples: Number of samples to generate.
    - block_size: Size of the encryption block.

    Returns:
    A list of dictionaries, each containing information about a plaintext avalanche sample.
    """
    dataset = []

    for _ in range(num_samples):
        # Generate a random plaintext
        plaintext = random.randint(0, 2 ** block_size - 1)

        # Encrypt the original plaintext
        original_ciphertext = encrypt(plaintext, generate_random_key())

        # Generate a slightly modified plaintext (e.g., flip one bit)
        modified_plaintext = plaintext ^ (1 << random.randint(0, block_size - 1))

        # Encrypt the modified plaintext
        modified_ciphertext = encrypt(modified_plaintext,generate_random_key())

        # Record the sample in the dataset
        dataset.append({
            'plaintext': plaintext,
            'modified_plaintext': modified_plaintext,
            'original_ciphertext': original_ciphertext,
            'modified_ciphertext': modified_ciphertext,
        })

    return dataset
