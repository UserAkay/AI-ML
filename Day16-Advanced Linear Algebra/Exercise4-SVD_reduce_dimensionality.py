import numpy as np

np.random.seed(42)
# Larger dataset: 100 samples, 10 features
data = np.random.rand(100, 10)

# Center the data
data_centered = data - data.mean(axis=0)

# Perform SVD
U, S, Vt = np.linalg.svd(data_centered, full_matrices=False)

print("Singular values:")
print(S)

# Reduce dimensionality to 2 components
k = 2
reduced_data = U[:, :k] * S[:k]

print(f"\nOriginal shape: {data.shape}")
print(f"Reduced shape: {reduced_data.shape}")
print("\nReduced data (first 5 rows):")
print(reduced_data[:5])