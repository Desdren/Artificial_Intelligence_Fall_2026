import numpy as np

# 1. Create 1D array
arr = np.array([5, 10, 15, 20, 25])

# 2. Display array information
print("Array:", arr)
print("Shape:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# 3. Add 10 to every element
print("After adding 10:", arr + 10)

# 4. Multiply every element by 3
print("After multiplying by 3:", arr * 3)

# 5. Find sum, mean, maximum and minimum
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 6. Create another array
arr2 = np.array([2, 4, 6, 8, 10])

# 7. Element-wise operations
print("Addition:", arr + arr2)
print("Subtraction:", arr - arr2)
print("Multiplication:", arr * arr2)
print("Division:", arr / arr2)