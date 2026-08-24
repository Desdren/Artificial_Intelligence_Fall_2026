import numpy as np

np.random.seed(42)

# --------------------------------------------------
# 1. Dataset
# --------------------------------------------------
# Features:
# Size, Bedrooms, Bathrooms, Age, Distance, Parking

X = np.array([
    [1000, 2, 1, 20, 15, 1],
    [1200, 2, 2, 15, 12, 1],
    [1500, 3, 2, 10, 10, 2],
    [1800, 3, 2, 8, 8, 2],
    [2000, 4, 3, 5, 6, 2],
    [2200, 4, 3, 4, 5, 3],
    [2500, 4, 3, 3, 4, 3],
    [2800, 5, 4, 2, 3, 3]
], dtype=float)

# House prices
y = np.array([
    [180000],
    [220000],
    [280000],
    [330000],
    [390000],
    [450000],
    [520000],
    [600000]
], dtype=float)

# --------------------------------------------------
# 2. Normalize X and y
# --------------------------------------------------

X_mean = X.mean(axis=0)
X_std = X.std(axis=0)

X_norm = (X - X_mean) / X_std

y_mean = y.mean()
y_std = y.std()

y_norm = (y - y_mean) / y_std

# --------------------------------------------------
# 3. Initialize weights and biases
# --------------------------------------------------

W1 = np.random.randn(6, 4) * 0.1
b1 = np.zeros((1, 4))

W2 = np.random.randn(4, 3) * 0.1
b2 = np.zeros((1, 3))

W3 = np.random.randn(3, 1) * 0.1
b3 = np.zeros((1, 1))


# --------------------------------------------------
# ReLU activation
# --------------------------------------------------

def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


# --------------------------------------------------
# 4. Training
# --------------------------------------------------

learning_rate = 0.01
epochs = 5000
m = len(X_norm)

for epoch in range(epochs):

    # ---------- Forward Propagation ----------

    z1 = np.dot(X_norm, W1) + b1
    a1 = relu(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = relu(z2)

    z3 = np.dot(a2, W3) + b3
    output = z3

    # ---------- Loss ----------

    loss = np.mean((output - y_norm) ** 2)

    # ---------- Backpropagation ----------

    dz3 = (2 / m) * (output - y_norm)

    dW3 = np.dot(a2.T, dz3)
    db3 = np.sum(dz3, axis=0, keepdims=True)

    da2 = np.dot(dz3, W3.T)
    dz2 = da2 * relu_derivative(z2)

    dW2 = np.dot(a1.T, dz2)
    db2 = np.sum(dz2, axis=0, keepdims=True)

    da1 = np.dot(dz2, W2.T)
    dz1 = da1 * relu_derivative(z1)

    dW1 = np.dot(X_norm.T, dz1)
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # ---------- Update weights ----------

    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Display loss every 500 epochs
    if (epoch + 1) % 500 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss:.6f}")

# --------------------------------------------------
# 5. Predict new house price
# --------------------------------------------------

new_house = np.array([
    [1800, 3, 2, 10, 8, 2]
], dtype=float)

# Normalize new input
new_house_norm = (new_house - X_mean) / X_std

# Forward propagation
z1 = np.dot(new_house_norm, W1) + b1
a1 = relu(z1)

z2 = np.dot(a1, W2) + b2
a2 = relu(z2)

z3 = np.dot(a2, W3) + b3
predicted_norm = z3

# Convert prediction back to original price
predicted_price = predicted_norm * y_std + y_mean

print("\nPredicted House Price:")
print(f"${predicted_price[0][0]:,.2f}")