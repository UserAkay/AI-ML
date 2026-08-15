import numpy as np
import matplotlib.pyplot as plt

#Cost Function (Mean Squared Error)
def compute_cost(X, y, theta):
    m = len(y)
    return (1 / (2 * m)) * np.sum((np.dot(X, theta) - y) ** 2)

#Gradient Descent Tracker
def gradient_descent_tracked(X, y, theta, lr, iterations):
    m = len(y)
    cost_history = []
    theta = theta.copy()  # Avoid modifying the original array
    
    for _ in range(iterations):
        errors = np.dot(X, theta) - y
        gradients = (1 / m) * np.dot(X.T, errors)
        theta -= lr * gradients
        cost_history.append(compute_cost(X, y, theta))
        
    return cost_history

#Setup Synthetic Data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]  # Add bias term (column of 1s)

#Compare Learning Rates
learning_rates = [0.01, 0.1, 0.5]
iterations = 50
initial_theta = np.random.randn(2, 1)

plt.figure(figsize=(10, 6))

for lr in learning_rates:
    history = gradient_descent_tracked(X_b, y, initial_theta, lr, iterations)
    plt.plot(range(iterations), history, label=f'lr = {lr}')

plt.title('Gradient Descent Convergence by Learning Rate')
plt.xlabel('Iterations')
plt.ylabel('Cost (MSE)')
plt.yscale('log')  # Log scale helps see dramatic divergence/convergence
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
