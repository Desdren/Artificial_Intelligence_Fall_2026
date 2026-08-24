import numpy as np

# Activation functions and their derivatives
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.int32(x > 0)

# 1. Create a synthetic dataset (Samples x Features)
# Features: [Size, Bedrooms, Bathrooms, Age, Distance, Parking]
np.random.seed(42)
X_raw = np.array([
    [1500, 3, 2, 15, 10, 1],
    [2000, 4, 3, 5, 5, 2],
    [1200, 2, 1, 25, 20, 1],
    [2500, 4, 3.5, 2, 3, 3],
    [1800, 3, 2, 10, 8, 2]
], dtype=float)

# Target values (House Prices in thousands)
y_raw = np.array([300, 450, 200, 600, 380], dtype=float).reshape(-1, 1)

# 2. Normalize input features and target values (Min-Max Scaling)
X_min, X_max = X_raw.min(axis=0), X_raw.max(axis=0)
y_min, y_max = y_raw.min(), y_raw.max()

X = (X_raw - X_min) / (X_max - X_min + 1e-8)
y = (y_raw - y_min) / (y_max - y_min + 1e-8)

# 3. Initialize Neural Network weights and biases
input_size = 6
hidden1_size = 4
hidden2_size = 3
output_size = 1

np.random.seed(42)
W1 = np.random.randn(input_size, hidden1_size) * 0.1
b1 = np.zeros((1, hidden1_size))
W2 = np.random.randn(hidden1_size, hidden2_size) * 0.1
b2 = np.zeros((1, hidden2_size))
W3 = np.random.randn(hidden2_size, output_size) * 0.1
b3 = np.zeros((1, output_size))

# 4. Training using Forward and Backpropagation
epochs = 5000
lr = 0.05

for epoch in range(epochs):
    # Forward Propagation
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    
    Z2 = np.dot(A1, W2) + b2
    A2 = relu(Z2)
    
    Z3 = np.dot(A2, W3) + b3
    y_pred = Z3  # Linear activation for output layer
    
    # Compute Loss (MSE)
    loss = np.mean((y_pred - y) ** 2)
    
    # 5. Display training loss every 500 epochs
    if (epoch + 1) % 500 == 0:
        print(f"Epoch {epoch + 1}/{epochs} - Loss: {loss:.6f}")
        
    # Backpropagation
    error = (y_pred - y) / X.shape[0]
    
    dW3 = np.dot(A2.T, error)
    db3 = np.sum(error, axis=0, keepdims=True)
    
    dA2 = np.dot(error, W3.T) * relu_derivative(Z2)
    dW2 = np.dot(A1.T, dA2)
    db2 = np.sum(dA2, axis=0, keepdims=True)
    
    dA1 = np.dot(dA2, W2.T) * relu_derivative(Z1)
    dW1 = np.dot(X.T, dA1)
    db1 = np.sum(dA1, axis=0, keepdims=True)
    
    # Update Weights & Biases
    W3 -= lr * dW3
    b3 -= lr * db3
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

# 6. Predict the price of a target house
house_to_predict = np.array([[1800, 3, 2, 10, 8, 2]], dtype=float)
house_normalized = (house_to_predict - X_min) / (X_max - X_min + 1e-8)

# Forward pass for prediction
p_Z1 = np.dot(house_normalized, W1) + b1
p_A1 = relu(p_Z1)
p_Z2 = np.dot(p_A1, W2) + b2
p_A2 = relu(p_Z2)
p_Z3 = np.dot(p_A2, W3) + b3

predicted_normalized = p_Z3[0, 0]
predicted_price = predicted_normalized * (y_max - y_min) + y_min

# 7. Display the predicted house price
print(f"\nPredicted House Price: ${predicted_price:.2f} (in thousands)")