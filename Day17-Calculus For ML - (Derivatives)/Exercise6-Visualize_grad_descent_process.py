import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

def df(x):
    return 2 * x


learning_rate = 0.2  
iterations = 10     
current_x = -4.0     


x_history = [current_x]
y_history = [f(current_x)]

for _ in range(iterations):
    current_x -= learning_rate * df(current_x)
    x_history.append(current_x)
    y_history.append(f(current_x))

#Create the Static Plot
x_curve = np.linspace(-5, 5, 100)
y_curve = f(x_curve)

plt.figure(figsize=(10, 6))

# Plot the underlying function curve
plt.plot(x_curve, y_curve, color='black', linewidth=2, label='f(x) = x²')

# Plot the steps taken by gradient descent
plt.plot(x_history, y_history, color='red', linestyle='--', marker='o', label='GD Steps')

# Highlight the starting and ending points
plt.scatter(x_history[0], y_history[0], color='blue', s=100, zorder=5, label='Start (-4, 16)')
plt.scatter(x_history[-1], y_history[-1], color='green', s=150, marker='*', zorder=5, label='End (Minimum)')

# Labels and Formatting
plt.title('Gradient Descent Steps on a Quadratic Curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
