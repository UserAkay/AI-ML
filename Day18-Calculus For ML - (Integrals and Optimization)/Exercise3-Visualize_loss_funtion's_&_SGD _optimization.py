"""
Exercise 3 (Simple Version)
Visualise a loss function and the path SGD takes while minimizing it.

Problem: fit y = w*x + b to some data points.
Loss = Mean Squared Error (MSE), which depends on w and b.
"""

import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Create simple data: y = 3x + 5 (plus some noise)
np.random.seed(0)
X = np.random.uniform(-5, 5, 50)
y = 3 * X + 5 + np.random.normal(0, 2, 50)


def loss_function(w, b):
    """Mean Squared Error for given w and b."""
    predictions = w * X + b
    return np.mean((predictions - y) ** 2)


# STEP 2: Run SGD starting from a bad guess, and record every step
w = -5.0   # starting guess (far from correct answer)
b = -10.0  # starting guess
learning_rate = 0.01
steps = 60

w_history = [w]
b_history = [b]

for i in range(steps):
    idx = np.random.randint(0, len(X))
    xi = X[idx]
    yi = y[idx]

    prediction = w * xi + b
    error = prediction - yi

    grad_w = 2 * error * xi
    grad_b = 2 * error

    w = w - learning_rate * grad_w
    b = b - learning_rate * grad_b

    w_history.append(w)
    b_history.append(b)

print(f"Final w = {w:.2f}, b = {b:.2f}  (target was w=3, b=5)")

# STEP 3: Draw a "map" of the loss for a grid of (w, b) values
w_range = np.linspace(-8, 8, 80)
b_range = np.linspace(-12, 12, 80)
W, B = np.meshgrid(w_range, b_range)

Loss = np.zeros(W.shape)
for i in range(W.shape[0]):
    for j in range(W.shape[1]):
        Loss[i, j] = loss_function(W[i, j], B[i, j])

# STEP 4: Plot the loss map + SGD path
plt.figure(figsize=(7, 6))
contour = plt.contour(W, B, Loss, levels=25, cmap="viridis")
plt.clabel(contour, inline=True, fontsize=7)

plt.plot(w_history, b_history, color="red", marker="o", markersize=3,
         linewidth=1, label="SGD path")
plt.scatter([3], [5], color="black", marker="*", s=150, label="True answer")

plt.xlabel("w")
plt.ylabel("b")
plt.title("Loss Map with SGD Path")
plt.legend()
plt.tight_layout()
plt.show()