import numpy as np

arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)
print(type(arr1))

# creating a 0-D array
arr = np.array(44)
print(arr)

# 1-D Array
'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.
'''

arr = np.array([1, 2, 3, 4, 5])

print(arr)

'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
'''
# creating a 2-D array containing 2 arrays with the values 1,2,3 and 4,5,6

ar2 = np.array([[1, 2, 3], [4, 5, 6]])
print(ar2)
print('\n')

'''
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor
'''
# Example
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

ar3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(ar3)
