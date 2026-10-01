import numpy as np

# 1. Create a 1D NumPy array
arr = np.array([5, 10, 15, 20, 25])

# 2. Display array details
print("Array:", arr)
print("Shape:", arr.shape)
print("Number of dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# 3. Add 10 to every element
added = arr + 10
print("\nAfter adding 10:", added)

# 4. Multiply every element by 3
multiplied = arr * 3
print("After multiplying by 3:", multiplied)

# 5. Sum, Mean, Maximum, Minimum
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 6. Create another array
arr2 = np.array([2, 4, 6, 8, 10])
print("\nSecond array:", arr2)

# 7. Element-wise operations
print("Addition:", arr + arr2)
print("Subtraction:", arr - arr2)
print("Multiplication:", arr * arr2)
print("Division:", arr / arr2)
