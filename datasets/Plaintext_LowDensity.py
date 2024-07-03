import random
import sys
import os
from baby_rijndael import babyr_enc

sys.path.append(os.getcwd())


def generate_low_density_dataset(size, density=0.2):
    """
    Generate a dataset with random low-density plaintexts and random keys.

    Args:
    - size: Number of pairs to generate.
    - density: Proportion of set bits in the plaintext (0.0 to 1.0).

    Returns:
    A list of tuples, each containing a low-density plaintext and a random key.
    """
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext with low density
        plaintext = 0
        for _ in range(16):
            if random.random() < density:
                plaintext |= 1 << random.randint(0, 15)

        # Generate a random 16-bit key
        key = random.randint(0, 0xFFFF)

        dataset.append((plaintext, key))
    return dataset