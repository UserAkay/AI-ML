"""
Exercise 4 (Simple Version)
Compare Vanilla SGD (1 data point per update) vs Mini-Batch SGD
(a small group of points per update).

Same problem as before: fit y = w*x + b to data.
"""

import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Data
np.random.seed(0)
X = np.random.uniform(-5, 5, 200)
y = 3 * X + 5 + np.random.normal(0, 2, 200)


def loss_function(w, b):
    predictions = w * X + b
    return np.mean((predictions - y) ** 2)


# STEP 2: Vanilla SGD -- update using ONE point at a time
def vanilla_sgd(learning_rate=0.01, epochs=50):
    w, b = -5.0, -10.0
    loss_per_epoch = []

    for epoch in range(epochs):
        order = np.random.permutation(len(X))
        for idx in order:
            xi = X[idx]
            yi = y[idx]

            prediction = w * xi + b
            error = prediction - yi

            grad_w = 2 * error * xi
            grad_b = 2 * error

            w = w - learning_rate * grad_w
            b = b - learning_rate * grad_b

        loss_per_epoch.append(loss_function(w, b))

    return w, b, loss_per_epoch


# STEP 3: Mini-Batch SGD -- update using a small GROUP of points
def minibatch_sgd(learning_rate=0.01, epochs=50, batch_size=16):
    w, b = -5.0, -10.0
    loss_per_epoch = []

    for epoch in range(epochs):
        order = np.random.permutation(len(X))
        for start in range(0, len(X), batch_size):
            batch_idx = order[start:start + batch_size]
            x_batch = X[batch_idx]
            y_batch = y[batch_idx]

            predictions = w * x_batch + b
            errors = predictions - y_batch

            grad_w = np.mean(2 * errors * x_batch)
            grad_b = np.mean(2 * errors)

            w = w - learning_rate * grad_w
            b = b - learning_rate * grad_b

        loss_per_epoch.append(loss_function(w, b))

    return w, b, loss_per_epoch


# STEP 4: Run both and compare
w1, b1, loss1 = vanilla_sgd()
w2, b2, loss2 = minibatch_sgd()

print("Vanilla SGD  -> w=%.2f, b=%.2f, final loss=%.3f" % (w1, b1, loss1[-1]))
print("Mini-Batch   -> w=%.2f, b=%.2f, final loss=%.3f" % (w2, b2, loss2[-1]))
print("Target was w=3, b=5")

# STEP 5: Plot loss curves for comparison
plt.figure(figsize=(8, 5))
plt.plot(loss1, label="Vanilla SGD (1 point at a time)", color="tomato")
plt.plot(loss2, label="Mini-Batch SGD (16 points at a time)", color="royalblue")
plt.xlabel("Epoch")
plt.ylabel("Loss (MSE)")
plt.title("Vanilla SGD vs Mini-Batch SGD")
plt.legend()
plt.tight_layout()
plt.show()