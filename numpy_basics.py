import numpy as np

# 1. Create a 1D NumPy array
arr = np.array([5, 10, 15, 20, 25])

# 2. Display array attributes
print("--- Array Attributes ---")
print(f"Array: {arr}")
print(f"Shape: {arr.shape}")
print(f"Number of dimensions: {arr.ndim}")
print(f"Size: {arr.size}")
print(f"Data type: {arr.dtype}")

# 3. Add 10 to every element
arr_plus_10 = arr + 10
print(f"\nArray after adding 10: {arr_plus_10}")

# 4. Multiply every element by 3
arr_mult_3 = arr * 3
print(f"Array after multiplying by 3: {arr_mult_3}")

# 5. Statistical operations
print("\n--- Statistics ---")
print(f"Sum: {np.sum(arr)}")
print(f"Mean: {np.mean(arr)}")
print(f"Maximum: {np.max(arr)}")
print(f"Minimum: {np.min(arr)}")

# 6. Create another array
arr2 = np.array([2, 4, 6, 8, 10])

# 7. Element-wise operations
print("\nElement-wise Operations with [2, 4, 6, 8, 10]")
print(f"Addition: {arr + arr2}")
print(f"Subtraction: {arr - arr2}")
print(f"Multiplication: {arr * arr2}")
print(f"Division: {arr / arr2}")