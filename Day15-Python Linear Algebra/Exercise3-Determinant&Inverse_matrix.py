import numpy as np

A = np.array([[2,3], [1, 4]])

determinant = np.linalg.det(A)
print("Determinant: ", determinant)

inverse = np.linalg.inv(A)
print("Inverse: \n", inverse)

#Compute determinant and inverse matrix
result = determinant + inverse
print("2*2 matrix: \n", result)