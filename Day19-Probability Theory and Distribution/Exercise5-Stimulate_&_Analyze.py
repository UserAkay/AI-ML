# Q. Use probability distributions to stimulate and analyze real-world datasets

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 5000

# Simulate a real-world dataset: daily customer data for a store
ages = np.random.normal(loc=35, scale=10, size=n).clip(18, 70)          # Gaussian: customer age
wait_times = np.random.exponential(scale=5, size=n)                     # Exponential: wait time (mins)
purchase_amount = np.random.gamma(shape=2, scale=20, size=n)            # Gamma: money spent ($)
visits_per_month = np.random.poisson(lam=4, size=n)                     # Poisson: store visits

# Analyze
print("---- Summary Statistics ----")
print(f"Age:        mean={ages.mean():.1f}, std={ages.std():.1f}")
print(f"Wait time:  mean={wait_times.mean():.1f} min, std={wait_times.std():.1f}")
print(f"Purchase:   mean=${purchase_amount.mean():.2f}, std=${purchase_amount.std():.2f}")
print(f"Visits/mo:  mean={visits_per_month.mean():.1f}, std={visits_per_month.std():.1f}")

# Visualize
fig, axes = plt.subplots(2, 2, figsize=(11, 8))

axes[0, 0].hist(ages, bins=40, color="steelblue", edgecolor="black")
axes[0, 0].set_title("Customer Age (Gaussian)")

axes[0, 1].hist(wait_times, bins=40, color="orange", edgecolor="black")
axes[0, 1].set_title("Wait Time in Minutes (Exponential)")

axes[1, 0].hist(purchase_amount, bins=40, color="seagreen", edgecolor="black")
axes[1, 0].set_title("Purchase Amount (Gamma)")

axes[1, 1].hist(visits_per_month, bins=range(0, 15), color="indianred", edgecolor="black")
axes[1, 1].set_title("Visits per Month (Poisson)")

plt.tight_layout()
plt.show()