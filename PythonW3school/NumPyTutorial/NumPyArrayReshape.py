'''
NumPy Array Reshaping
Reshaping arrays
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.
'''
# reshape from 1-d to 2-d
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newArr = arr.reshape(4, 3)
print(newArr)
# Example
'''
Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
'''

arr3d = arr.reshape(2, 3, 2)
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)
# to check if the returned array is copy or a view
# the above example gives the original array so its a view and not a copy
print(newArr.base)
print(arr3d.base)

'''
Unknown Dimension
You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you.
'''
# Convert 1D array with 8 elements to 3D array with 2x2 elements:

arrD = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newArD = arrD.reshape(2, 2, -1)
print(arrD)
print(arrD.ndim)
print(arrD.shape)
print(newArD)

'''
Flattening the arrays
Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.
'''
# converting a array into 1d

arC = np.array([[1, 2, 3], [4, 5, 6]])
print(arC)
print(arC.ndim)
print(arC.shape)

convert = arC.reshape(-1)  # to make it flatten 1-d array
print(convert)
