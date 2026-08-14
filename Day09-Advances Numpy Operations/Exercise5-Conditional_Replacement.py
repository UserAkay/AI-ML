import numpy as np

# Generate a dataset of random floats
np.random.seed(7)
values = np.random.uniform(0, 100, 12).round(2)
print("Original values: ", values)

# Set a threshold
threshold = 50.0

# Conditional replacement: create a binary mark
# 1 if value > threshold, else 0
binary_mark = np.where(values > threshold, 1, 0)

print("Threshold: ", threshold)
print("Binary marks (1 if above threshold, else 0): ", binary_mark)
