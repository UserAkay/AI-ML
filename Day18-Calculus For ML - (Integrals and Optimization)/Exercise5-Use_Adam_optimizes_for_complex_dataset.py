"""
Exercise 5 (Fixed - within your learned topics only)
Use the Adam optimizer on a "more complex" dataset than Exercise3/4.

Instead of a neural network (which needs topics you haven't covered
yet, like backpropagation), we make the problem harder in a way that
only uses what you already know:

  Exercise 3/4 fit a STRAIGHT LINE:  y = w*x + b        (2 parameters)
  This exercise fits a CURVE:        y = a*x^2 + b*x + c (3 parameters)

Everything here uses only: loops, NumPy arrays, gradients (derivatives),
and Matplotlib -- same tools as your earlier exercises.
"""

import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Create curved (non-linear) data
# True curve: y = 2x^2 + 3x + 5
np.random.seed(0)
X = np.random.uniform(-5, 5, 200)
true_a, true_b, true_c = 2.0, 3.0, 5.0
y = true_a * X**2 + true_b * X + true_c + np.random.normal(0, 5, 200)


def predict(a, b, c, X):
    return a * X**2 + b * X + c


def loss_function(a, b, c):
    predictions = predict(a, b, c, X)
    return np.mean((predictions - y) ** 2)


def gradients(a, b, c, x_batch, y_batch):
    """Derivative of MSE loss with respect to a, b, c for a batch of points."""
    predictions = predict(a, b, c, x_batch)
    error = predictions - y_batch
    grad_a = np.mean(2 * error * x_batch**2)
    grad_b = np.mean(2 * error * x_batch)
    grad_c = np.mean(2 * error)
    return grad_a, grad_b, grad_c


# STEP 2: Plain SGD (mini-batch style, same as Exercise 4)
def train_sgd(learning_rate=0.001, epochs=200, batch_size=16):
    a, b, c = 0.0, 0.0, 0.0   # start from zero
    loss_history = []

    for epoch in range(epochs):
        order = np.random.permutation(len(X))
        for start in range(0, len(X), batch_size):
            batch_idx = order[start:start + batch_size]
            x_batch = X[batch_idx]
            y_batch = y[batch_idx]

            grad_a, grad_b, grad_c = gradients(a, b, c, x_batch, y_batch)

            a = a - learning_rate * grad_a
            b = b - learning_rate * grad_b
            c = c - learning_rate * grad_c

        loss_history.append(loss_function(a, b, c))

    return a, b, c, loss_history


# STEP 3: Adam optimizer (mini-batch style)
# Adam keeps two "memory" values per parameter:
#   m = running average of the gradient        (momentum)
#   v = running average of the gradient squared (scale)
# Then it uses m and v together to decide the step size.
def train_adam(learning_rate=0.05, epochs=200, batch_size=16):
    a, b, c = 0.0, 0.0, 0.0

    beta1 = 0.9
    beta2 = 0.999
    epsilon = 1e-8

    # memory values, one for each parameter, start at zero
    m_a, v_a = 0.0, 0.0
    m_b, v_b = 0.0, 0.0
    m_c, v_c = 0.0, 0.0

    loss_history = []
    t = 0  # counts total updates done so far

    for epoch in range(epochs):
        order = np.random.permutation(len(X))
        for start in range(0, len(X), batch_size):
            t += 1
            batch_idx = order[start:start + batch_size]
            x_batch = X[batch_idx]
            y_batch = y[batch_idx]

            grad_a, grad_b, grad_c = gradients(a, b, c, x_batch, y_batch)

            # --- update memory for a ---
            m_a = beta1 * m_a + (1 - beta1) * grad_a
            v_a = beta2 * v_a + (1 - beta2) * (grad_a ** 2)
            m_a_hat = m_a / (1 - beta1 ** t)
            v_a_hat = v_a / (1 - beta2 ** t)
            a = a - learning_rate * m_a_hat / (np.sqrt(v_a_hat) + epsilon)

            # --- update memory for b ---
            m_b = beta1 * m_b + (1 - beta1) * grad_b
            v_b = beta2 * v_b + (1 - beta2) * (grad_b ** 2)
            m_b_hat = m_b / (1 - beta1 ** t)
            v_b_hat = v_b / (1 - beta2 ** t)
            b = b - learning_rate * m_b_hat / (np.sqrt(v_b_hat) + epsilon)

            # --- update memory for c ---
            m_c = beta1 * m_c + (1 - beta1) * grad_c
            v_c = beta2 * v_c + (1 - beta2) * (grad_c ** 2)
            m_c_hat = m_c / (1 - beta1 ** t)
            v_c_hat = v_c / (1 - beta2 ** t)
            c = c - learning_rate * m_c_hat / (np.sqrt(v_c_hat) + epsilon)

        loss_history.append(loss_function(a, b, c))

    return a, b, c, loss_history


# STEP 4: Run both and compare
a_sgd, b_sgd, c_sgd, loss_sgd = train_sgd()
a_adam, b_adam, c_adam, loss_adam = train_adam()

print("SGD  -> a=%.2f, b=%.2f, c=%.2f, final loss=%.2f" % (a_sgd, b_sgd, c_sgd, loss_sgd[-1]))
print("Adam -> a=%.2f, b=%.2f, c=%.2f, final loss=%.2f" % (a_adam, b_adam, c_adam, loss_adam[-1]))
print("Target: a=2, b=3, c=5")

# STEP 5: Plot loss curves + the fitted curves on the data
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].plot(loss_sgd, label="SGD", color="tomato")
axes[0].plot(loss_adam, label="Adam", color="royalblue")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss (MSE)")
axes[0].set_title("Loss per Epoch: SGD vs Adam")
axes[0].legend()

x_line = np.linspace(-5, 5, 100)
axes[1].scatter(X, y, color="gray", alpha=0.4, s=15, label="Data")
axes[1].plot(x_line, predict(a_sgd, b_sgd, c_sgd, x_line), color="tomato",
             linewidth=2, label="SGD fit")
axes[1].plot(x_line, predict(a_adam, b_adam, c_adam, x_line), color="royalblue",
             linewidth=2, label="Adam fit")
axes[1].plot(x_line, predict(true_a, true_b, true_c, x_line), color="black",
             linestyle="--", linewidth=1.5, label="True curve")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].set_title("Fitted Curves vs Data")
axes[1].legend()

plt.tight_layout()
plt.show()