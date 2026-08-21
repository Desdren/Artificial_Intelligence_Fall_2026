import numpy as np

# Question 2: Neural Network for House Price Prediction
# The assignment does not provide exact dataset values, so this program
# uses a small illustrative dataset. Replace it with the dataset you are given
# by your instructor if one is provided separately.

np.random.seed(42)

# Features:
# [House Size, Bedrooms, Bathrooms, House Age, Distance from City, Parking Spaces]
X = np.array([
    [1000, 2, 1, 20, 15, 1],
    [1200, 2, 2, 15, 12, 1],
    [1400, 3, 2, 12, 10, 1],
    [1600, 3, 2, 10, 8, 2],
    [1800, 3, 2, 10, 8, 2],
    [2000, 4, 3, 7, 6, 2],
    [2200, 4, 3, 5, 5, 2],
    [2500, 4, 3, 4, 4, 3],
    [2800, 5, 4, 3, 3, 3],
    [3000, 5, 4, 2, 2, 3],
], dtype=float)

# Target: house price in NPR
y = np.array([
    6500000,
    7600000,
    9000000,
    10500000,
    11500000,
    13000000,
    14500000,
    16500000,
    19000000,
    21000000,
], dtype=float).reshape(-1, 1)


# ---------- Normalization ----------
def min_max_scale(data):
    data_min = data.min(axis=0)
    data_max = data.max(axis=0)
    scaled = (data - data_min) / (data_max - data_min)
    return scaled, data_min, data_max


def min_max_inverse(scaled, data_min, data_max):
    return scaled * (data_max - data_min) + data_min


X_norm, X_min, X_max = min_max_scale(X)
y_norm, y_min, y_max = min_max_scale(y)


# ---------- Activation functions ----------
def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


# ---------- Network ----------
# 6 input neurons -> 4 hidden neurons -> 3 hidden neurons -> 1 output neuron
W1 = np.random.randn(6, 4) * 0.1
b1 = np.zeros((1, 4))

W2 = np.random.randn(4, 3) * 0.1
b2 = np.zeros((1, 3))

W3 = np.random.randn(3, 1) * 0.1
b3 = np.zeros((1, 1))

learning_rate = 0.05
epochs = 5000


# ---------- Training ----------
for epoch in range(1, epochs + 1):
    # Forward propagation
    z1 = X_norm @ W1 + b1
    a1 = relu(z1)

    z2 = a1 @ W2 + b2
    a2 = relu(z2)

    z3 = a2 @ W3 + b3
    output = z3  # Linear output for regression

    # Mean squared error
    error = output - y_norm
    loss = np.mean(error ** 2)

    # Backpropagation
    d_output = (2 / len(X_norm)) * error

    dW3 = a2.T @ d_output
    db3 = np.sum(d_output, axis=0, keepdims=True)

    da2 = d_output @ W3.T
    dz2 = da2 * relu_derivative(z2)

    dW2 = a1.T @ dz2
    db2 = np.sum(dz2, axis=0, keepdims=True)

    da1 = dz2 @ W2.T
    dz1 = da1 * relu_derivative(z1)

    dW1 = X_norm.T @ dz1
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # Gradient descent
    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")


# ---------- Prediction ----------
new_house = np.array([[1800, 3, 2, 10, 8, 2]], dtype=float)
new_house_norm = (new_house - X_min) / (X_max - X_min)

z1 = new_house_norm @ W1 + b1
a1 = relu(z1)

z2 = a1 @ W2 + b2
a2 = relu(z2)

z3 = a2 @ W3 + b3
predicted_norm = z3

predicted_price = min_max_inverse(predicted_norm, y_min, y_max)

print("\nHouse to predict:")
print("Size = 1800")
print("Bedrooms = 3")
print("Bathrooms = 2")
print("Age = 10")
print("Distance = 8")
print("Parking = 2")

print(f"\nPredicted house price: NPR {predicted_price[0, 0]:,.2f}")
