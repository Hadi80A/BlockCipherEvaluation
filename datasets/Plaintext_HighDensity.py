import random
import sys
import numpy as np
import os
from baby_rijndael import babyr_enc

sys.path.append(os.getcwd())


def generate_high_density_plaintext_dataset(size, plaintext_density=0.8, key_density=0.8):
    """
    Generate a dataset with random high-density plaintexts and keys.

    Args:
    - size: Number of pairs to generate.
    - plaintext_density: Proportion of set bits in the plaintext (0.0 to 1.0).
    - key_density: Proportion of set bits in the key (0.0 to 1.0).

    Returns:
    A list of tuples, each containing a high-density plaintext and a high-density key.
    """
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext with high density
        plaintext = 0
        for i in range(16):
            if random.random() < plaintext_density:
                plaintext |= 1 << i

        # Generate a random 16-bit key with high density
        key = 0
        for i in range(16):
            if random.random() < key_density:
                key |= 1 << i

        dataset.append((plaintext, key))
    return dataset