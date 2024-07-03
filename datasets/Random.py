import numpy as np
import sys
import os
import random
from baby_rijndael import babyr_enc, babyr_dec

# Add the current working directory to the system path
sys.path.append(os.getcwd())

# Import necessary functions from the cipher_algorithm module


def generate_random_dataset(size):
    """
    Generate a random dataset of block-key pairs.

    Args:
    - size: Number of random pairs to generate.

    Returns:
    A list of tuples, each containing a random 16-bit block and key.
    """
    dataset = []
    for _ in range(size):
        # Generating random 16-bit block and key
        block = random.randint(0, 0xFFFF)
        key = random.randint(0, 0xFFFF)
        dataset.append((block, key))
    return dataset
