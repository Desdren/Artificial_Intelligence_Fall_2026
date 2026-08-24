# House Price Prediction using Artificial Neural Network (ANN)


import numpy as np

# Dataset
X = np.array([
    [1000, 2, 1, 20, 10, 1],
    [1200, 2, 2, 15, 8, 1],
    [1500, 3, 2, 10, 5, 2],
    [1800, 3, 2, 10, 8, 2],
    [2000, 4, 3, 5, 4, 3],
    [2200, 4, 3, 3, 3, 3],
    [2500, 5, 3, 2, 2, 4],
    [2800, 5, 4, 1, 2, 4]
], dtype=float)

# Target house prices
y = np.array([
    [300],
    [350],
    [450],
    [500],
    [600],
    [650],
    [750],
    [850]
], dtype=float)

# Normalize input and target
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X = (X - X_min) / (X_max - X_min)

y_min = y.min()
y_max = y.max()
y = (y - y_min) / (y_max - y_min)

# Initialize weights and biases
np.random.seed(1)

W1 = np.random.randn(6, 4) * 0.1
b1 = np.zeros((1, 4))

W2 = np.random.randn(4, 3) * 0.1
b2 = np.zeros((1, 3))

W3 = np.random.randn(3, 1) * 0.1
b3 = np.zeros((1, 1))

learning_rate = 0.01

# ReLU function
def relu(x):
    return np.maximum(0, x)

# ReLU derivative
def relu_derivative(x):
    return (x > 0).astype(float)

# Training
for epoch in range(1, 5001):

    # Forward propagation
    z1 = np.dot(X, W1) + b1
    a1 = relu(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = relu(z2)

    output = np.dot(a2, W3) + b3

    # Loss
    loss = np.mean((output - y) ** 2)

    # Backpropagation
    d_output = 2 * (output - y) / len(y)

    dW3 = np.dot(a2.T, d_output)
    db3 = np.sum(d_output, axis=0, keepdims=True)

    da2 = np.dot(d_output, W3.T)
    dz2 = da2 * relu_derivative(z2)

    dW2 = np.dot(a1.T, dz2)
    db2 = np.sum(dz2, axis=0, keepdims=True)

    da1 = np.dot(dz2, W2.T)
    dz1 = da1 * relu_derivative(z1)

    dW1 = np.dot(X.T, dz1)
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # Update weights
    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Display loss every 500 epochs
    if epoch % 500 == 0:
        print("Epoch:", epoch, "Loss:", loss)

# Prediction
house = np.array([[1800, 3, 2, 10, 8, 2]], dtype=float)

# Normalize input
house = (house - X_min) / (X_max - X_min)

# Forward propagation for prediction
a1 = relu(np.dot(house, W1) + b1)
a2 = relu(np.dot(a1, W2) + b2)
prediction = np.dot(a2, W3) + b3

# Convert back to original price
price = prediction * (y_max - y_min) + y_min

print("Predicted House Price:", price[0][0])