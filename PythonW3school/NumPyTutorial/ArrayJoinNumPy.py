'''
NumPy Joining Array
Joining NumPy Arrays
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
'''

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
ar2 = np.array([5, 4, 3, 2, 1])

arr = np.concatenate((arr1, ar2), axis=0)
print(arr1)
print(ar2)
print(arr)

'''
Joining Arrays Using Stack Functions
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
'''

ar1 = np.array([1, 2, 3, 4])
ar2 = np.array([5, 6, 7, 8])

Arr = np.stack((ar1, ar2), axis=1)

print("The join of arrays using stack() is  "'\n', Arr)

# stacking along rows
# NumPy provides a helper function :hstack() to stack along rows

ArrH = np.hstack((ar1, ar2))
print("The horizontal stacking is ", ArrH)

'''

Stacking Along Columns
NumPy provides a helper function: vstack()  to stack along columns.
'''

ArrV = np.vstack((ar1, ar2))
print("The vertical stacking obtained using vstack() is"'\n', ArrV)

'''
Stacking Along Height (depth)
NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
'''

ArrD = np.dstack((ar1, ar2))
print("The stacking along the depth using dstack() is "'\n', ArrD)
