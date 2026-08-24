import numpy as np

# Question 1: NumPy Basics

arr1 = np.array([5, 10, 15, 20, 25])

print("Original array:", arr1)
print("Shape:", arr1.shape)
print("Number of dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)

print("\nArray + 10:", arr1 + 10)
print("Array * 3:", arr1 * 3)

print("\nSum:", arr1.sum())
print("Mean:", arr1.mean())
print("Maximum:", arr1.max())
print("Minimum:", arr1.min())

arr2 = np.array([2, 4, 6, 8, 10])

print("\nSecond array:", arr2)
print("Element-wise addition:", arr1 + arr2)
print("Element-wise subtraction:", arr1 - arr2)
print("Element-wise multiplication:", arr1 * arr2)
print("Element-wise division:", arr1 / arr2)
