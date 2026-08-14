import numpy as np

# Generate a 3D random array
random_array = np.random.rand(2, 3, 4)
print("Random 3D Array (shape 2x3x4): \n", random_array)

# Compute statistics along specific axes
# axis=0: across the 2 depth slices
print("\nMean along axis 0: \n", np.mean(random_array, axis=0))
print("\nSum along axis 1: \n", np.sum(random_array, axis=1))
print("\nStandard deviation along axis 2: \n", np.std(random_array, axis=2))

# Overall statistics
print("\nOverall Mean: ", np.mean(random_array))
print("Overall Max: ", np.max(random_array))
print("Overall Min: ", np.min(random_array))
