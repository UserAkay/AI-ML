import numpy as np

# Generate a dataset of random floats (e.g., 50 values between 0 and 100)
np.random.seed(42)  # for reproducible results
dataset = np.random.uniform(0, 100, 50)
print("Original dataset (first 10): ", dataset[:10])
print("Original min: ", dataset.min(), "| Original max: ", dataset.max())

# Normalize the values between 0 and 1 using min-max normalization
min_val = dataset.min()
max_val = dataset.max()
normalized = (dataset - min_val) / (max_val - min_val)

print("\nNormalized dataset (first 10): ", normalized[:10])
print("Normalized min: ", normalized.min(), "| Normalized max: ", normalized.max())
