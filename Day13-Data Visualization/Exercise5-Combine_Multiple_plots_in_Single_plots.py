import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Line Plot")

axs[0, 1].scatter(x, np.cos(x))
axs[0, 1].set_title("Scatter Plot")

axs[1, 0].bar(["A", "B", "C"], [10, 20, 15])
axs[1, 0].set_title("Bar Plot")

axs[1, 1].hist(np.random.normal(size=200), bins=20)
axs[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()