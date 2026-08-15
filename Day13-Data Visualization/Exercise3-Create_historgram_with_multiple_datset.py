import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
dataset1 = np.random.normal(loc=50, scale=10, size=200)
dataset2 = np.random.normal(loc=65, scale=15, size=200)

plt.hist(dataset1, bins=20, alpha=0.5, label="Dataset 1")
plt.hist(dataset2, bins=20, alpha=0.5, label="Dataset 2")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Overlaid Histograms of Two Datasets")
plt.legend()
plt.show()