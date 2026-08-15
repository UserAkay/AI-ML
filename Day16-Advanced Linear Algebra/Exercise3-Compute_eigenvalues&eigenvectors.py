import numpy as np

np.random.seed(42)
# Larger dataset: 100 samples, 5 features
data = np.random.rand(100, 5)

# Compute covariance matrix of the features
cov_matrix = np.cov(data, rowvar=False)
print("Covariance matrix:")
print(cov_matrix)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)