import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest, ks_2samp
from datasets.Avalanch_Key import avalanche_key_dataset
from datasets.Avalanch_Plaintext import plaintext_avalanche_dataset
from datasets.Correlation_PlainCipher import plaintext_ciphertext_correlation_dataset
from datasets.CBC import generate_cbc_dataset
from datasets.Key_HighDensity import generate_high_density_key_dataset
from datasets.Key_LowDensity import generate_low_density_key_dataset
from datasets.Plaintext_HighDensity import generate_high_density_plaintext_dataset
from datasets.Plaintext_LowDensity import generate_low_density_dataset
from datasets.Random import generate_random_dataset
from baby_rijndael import babyr_enc

result={}

def main():
    datasets = generate_data()
    for name, dataset in datasets.items():
        print(f"{name}:")
        result[name]=[]
        for data in dataset:
            value= uniform_test(data)
            result[name].append(value)
        print("~"*60)


def binary(x):
    n = 0
    for i in x:
        n *= 16
        n += i
    return bin(n)[2:]


def generate_data():
    n_samples = 16
    av_key = avalanche_key_dataset(None, num_samples=n_samples)
    plaintext_avalanche = plaintext_avalanche_dataset(None, num_samples=n_samples)
    cbc = generate_cbc_dataset(size=1)
    corr = plaintext_ciphertext_correlation_dataset(None, num_samples=n_samples)
    key_high = generate_high_density_key_dataset(n_samples)
    key_low = generate_low_density_key_dataset(n_samples)
    plain_low = generate_low_density_dataset(n_samples)
    plain_high = generate_high_density_plaintext_dataset(n_samples)
    rand = generate_random_dataset(n_samples)
    datasets = {
        'Avalanch_Key': [binary(data['modified_ciphertext']) for data in av_key],
        'Avalanch_Plaintext': [binary(data['modified_ciphertext']) for data in plaintext_avalanche],
        'CBC': [binary(babyr_enc(data[0], data[1])) for data in cbc],
        'Correlation_PlainCipher': [binary(data['ciphertext']) for data in corr],
        'Key_HighDensity': [binary(babyr_enc(data[0], data[1])) for data in key_high],
        'Key_LowDensity': [binary(babyr_enc(data[0], data[1])) for data in key_low],
        'Plaintext_HighDensity': [binary(babyr_enc(data[0], data[1])) for data in plain_high],
        'Plaintext_LowDensity': [binary(babyr_enc(data[0], data[1])) for data in plain_low],
        'Random': [binary(babyr_enc(data[0], data[1])) for data in rand],

    }
    return datasets


def uniform_test(values):
    values = [int(x) for x in values]
    np.random.seed(42)
    uniform_dist = np.random.uniform(0, 1, len(values))
    ks_statistic, p_value = kstest(values, uniform_dist)

    alpha = 0.05  # significance level
    if p_value < alpha:
        print(" The sample does not follow a uniform distribution ❌")
    else:
        print(" The sample follows a uniform distribution.        ✅")
    return p_value


def plot_results():
    fig, axs = plt.subplots(3, 3, figsize=(12, 10))
    axs = axs.flatten()

    for i, (title, values) in enumerate(result.items()):
        ax = axs[i]
        ax.scatter(range(len(values)), values)
        ax.axhline(y=0.05, color='r', linestyle='--')
        ax.set_title(title)
        ax.set_xlabel('Index')
        ax.set_ylabel('p-value')
        ax.grid(True)

    # Adjust layout
    plt.tight_layout()
    plt.savefig('plot.png')


if __name__ == '__main__':
    main()
    plot_results()
