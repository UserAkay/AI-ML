# Q. Compare Gaussian and Uniform Distribution for continuous data

import numpy as np
import matplotlib.pyplot as plt

n = 10000

gaussian_data = np.random.normal(loc=0, scale=1, size=n)
uniform_data = np.random.uniform(low=-3, hish=3, size=n)

plt.hist(gaussian_data, bins=50, alpha=0.6, label="Gaussain", color="royalblue", density=True)
plt.hist(uniform_data, bins=50, alpha=0.6, label="Uniform", color="orange", density="True")

plt.title("Gaussain vs Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()