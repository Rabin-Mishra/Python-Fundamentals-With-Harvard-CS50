'''
NumPy Array Slicing
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
'''

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
# Note: The result includes the start index, but excludes the end index.
print(arr[1:5])

print(arr[4:])

print(arr[:4])


'''
Negative Slicing
Use the minus operator to refer to an index from the end:
'''

print(arr[-3:-1])

# using the step value to determine the step f slicing

print(arr[1:5:2])

# from the start to the very end to get every other element from the entire array
print(arr[::2])

# slicing 2d arrays
# from the second element slice the elements from index1 to index4

ar1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(ar1[1, 1:4])
# Note: Remember that second element has index 1.

# Example
# From both elements, return index 2:
print(ar1[0:2, 2])

#Example
#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(ar1[0:2, 1:4])