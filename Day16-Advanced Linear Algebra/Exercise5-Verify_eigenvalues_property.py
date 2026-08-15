import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:")
print(eigenvalues)

# Verify det(A - lambda * I) = 0 for each eigenvalue
identity = np.eye(A.shape[0])

for lam in eigenvalues:
    result_matrix = A - lam * identity
    determinant = np.linalg.det(result_matrix)
    print(f"\nFor lambda = {lam:.4f}:")
    print(f"det(A - lambda*I) = {determinant:.10f}")
    print("This is approximately 0, confirming lambda is a valid eigenvalue.")