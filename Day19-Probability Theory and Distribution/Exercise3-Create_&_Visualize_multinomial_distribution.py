# Q. Create and visualize a multinomial distribution for multi-class data

import numpy as np
import matplotlib.pyplot as plt

classes =["A", "B", "C", "D"]
probs = [0.2, 0.3, 0.35, 0.15]
n_trials = 1000

counts = np.random.multinomial(n_trials, probs)

plt.bar(classes, counts, color="skyblue", edgecolor = "black")
plt.title("Multinomial Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()