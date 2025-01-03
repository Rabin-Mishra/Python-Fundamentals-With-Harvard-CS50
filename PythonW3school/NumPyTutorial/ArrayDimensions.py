'''
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

'''
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("Dimension of array of a=", a.ndim)
print("Dimension of array of b=", b.ndim)
print("Dimension of array of c=", c.ndim)
print("Dimension of array of d=", d.ndim)

# for creating any number of dimensions we will be using an argument ndmin
'''
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
'''
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("Number of dimensions :", arr.ndim)
