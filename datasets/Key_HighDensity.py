import random
import sys
import os
from baby_rijndael import babyr_enc, print_b

sys.path.append(os.getcwd())


def generate_high_density_key_dataset(size, key_density=0.8):
    """
    Generate a dataset with random plaintexts and high-density keys.

    Args:
    - size: Number of pairs to generate.
    - key_density: Proportion of set bits in the key (0.0 to 1.0).

    Returns:
    A list of tuples, each containing a plaintext and a high-density key.
    """
    dataset = []
    for _ in range(size):
        # Generate a random 16-bit plaintext
        plaintext = random.randint(0, 0xFFFF)

        # Generate a random 16-bit key with high density
        key = 0
        for i in range(16):
            if random.random() < key_density:
                key |= 1 << i

        dataset.append((plaintext, key))
    return dataset
