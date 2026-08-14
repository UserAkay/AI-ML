import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
print("4x4 Matrix: \n", matrix)

# Calculate the sum of each row
row_sums = np.sum(matrix, axis=1)
print("Sum of each row: ", row_sums)

# Calculate the sum of each column
col_sums = np.sum(matrix, axis=0)
print("Sum of each column: ", col_sums)
