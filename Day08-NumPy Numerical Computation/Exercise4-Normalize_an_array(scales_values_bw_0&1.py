import numpy as np

# Create an array
arr = np.array([2, 4, 6, 8, 10, 12, 14, 16])
print("Original array: ", arr)

# Min-Max normalization: scale values between 0 and 1
min_val = arr.min()
max_val = arr.max()
normalized = (arr - min_val) / (max_val - min_val)

print("Normalized array (0 to 1): ", normalized)
print("Min of normalized: ", normalized.min())
print("Max of normalized: ", normalized.max())
