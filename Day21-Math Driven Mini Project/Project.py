#Linear Regression from Scratch

# Task1: Implement the Mathematical Formula for linear Regression
import numpy as np

#Generate Synthetic data
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

#Add bias term to feature matrix
x_b = np.c_[np.ones((100, 1)), x]

#Initialize parameters
theta = np.random.randn(2, 1)
learning_rate = 0.1
iterations = 1000


def predict(x, theta):
    return np.dot(x, theta)

# Task2: Use Gradient Descent to Optimize the Model Parameters

def gradient_descent(x, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        gradients = (1/m) * np.dot(x.T, (np.dot(x, theta) - y))
        theta -= learning_rate * gradients
        return theta

# Task3: Calculate Evaluation Metrics

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) **2)


def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) **2)
    ss_tot = np.sum((y_true - np.mean(y_true)) **2)
    return 1 - (ss_res / ss_tot)


#Perform gradient descent

theta_optimized = gradient_descent(x_b, y, theta, learning_rate, iterations)

#Predictions and evaluations
y_pred = predict(x_b, theta_optimized)
mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized Parameters (Theta):", theta_optimized)
print("MSE: ", mse)
print("R2: ", r2)