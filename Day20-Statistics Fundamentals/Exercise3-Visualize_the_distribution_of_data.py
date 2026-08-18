# Q. Visualize the distribution of data and highlight mean, median, and mode using Matplotlib

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
data = np.random.gamma(shape=2, scale=20, size=2000)  # skewed dataset

mean_val = np.mean(data)
median_val = np.median(data)
mode_val = stats.mode(data.round(), keepdims=True).mode[0]

plt.hist(data, bins=50, color="skyblue", edgecolor="black", alpha=0.7)

plt.axvline(mean_val, color="red", linestyle="--", linewidth=2, label=f"Mean = {mean_val:.2f}")
plt.axvline(median_val, color="green", linestyle="--", linewidth=2, label=f"Median = {median_val:.2f}")
plt.axvline(mode_val, color="purple", linestyle="--", linewidth=2, label=f"Mode = {mode_val:.2f}")

plt.title("Data Distribution with Mean, Median, and Mode")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()