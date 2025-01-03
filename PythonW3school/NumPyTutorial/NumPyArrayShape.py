'''
NumPy Array Shape
Shape of an Array
The shape of an array is the number of elements in each dimension.

Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.      
'''
import numpy as np

arr = np.array([[1, 2, 3, 4], [6, 5, 4, 3]])
print(arr)

print(arr.ndim)
# The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.
print(arr.shape)

ar1 = np.array([1, 2, 3, 4], ndmin=5)
print(ar1.ndim)
print(ar1)
print(ar1.shape)
