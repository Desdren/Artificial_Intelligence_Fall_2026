import numpy as np

# 1. Create a 1D NumPy array
arr1 = np.array([5, 10, 15, 20, 25])

# 2. Display array properties
print("Original Array:", arr1)
print("Shape:", arr1.shape)
print("Number of Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)

# 3. Add 10 to every element
add_10 = arr1 + 10
print("\nAfter adding 10:", add_10)

# 4. Multiply every element by 3
multiply_3 = arr1 * 3
print("After multiplying by 3:", multiply_3)

# 5. Statistical operations
print("\nSum:", arr1.sum())
print("Mean:", arr1.mean())
print("Maximum:", arr1.max())
print("Minimum:", arr1.min())

# 6. Create another array
arr2 = np.array([2, 4, 6, 8, 10])

print("\nSecond Array:", arr2)

# 7. Element-wise operations
print("\nElement-wise Addition:", arr1 + arr2)
print("Element-wise Subtraction:", arr1 - arr2)
print("Element-wise Multiplication:", arr1 * arr2)
print("Element-wise Division:", arr1 / arr2)