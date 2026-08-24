# numpy library basics


import numpy as np

arr1 = np.array([11, 13, 17, 19, 23])

# basic properties of the array
print("Array:", arr1)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)

# adding and multiplying array with scalar values
arr_add10 = arr1 + 10
print("Add 10 to every element:", arr_add10)

arr_mul3 = arr1 * 3
print("Multiply every element by 3:", arr_mul3)

# basic statistical operations
print("Sum:", arr1.sum())
print("Mean:", arr1.mean())
print("Maximum:", arr1.max())
print("Minimum:", arr1.min())

arr2 = np.array([9, 19, 29, 39, 49])

# element-wise operations between two arrays
print("Element-wise Addition:", arr1 + arr2)
print("Element-wise Subtraction:", arr1 - arr2)
print("Element-wise Multiplication:", arr1 * arr2)
print("Element-wise Division:", arr1 / arr2)
