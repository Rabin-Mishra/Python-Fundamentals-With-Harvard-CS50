'''
NumPy Array Iterating
Iterating Arrays
Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.
'''
# Iterate on the elements of the following 1-D array:
import numpy as np
arr = np.array([1, 2, 3])

for x in arr:
    print(x)

'''
Iterating 2-D Arrays
In a 2-D array it will go through all the rows.
'''
# Iterate on the elements of the following 2-D array:

ar2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in ar2:
    print(x)

# To return the actual values, the scalars, we have to iterate the arrays in each dimension.
# Iterate on each scalar element of the 2-D array:

for x in ar2:
    for y in x:
        print(y)

'''
Iterating 3-D Arrays
In a 3-D array it will go through all the 2-D arrays.
'''
ar3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in ar3:
    print("x represents the 2-D array:")
    print(x)

# iterating down to the scalars for the 3d array
for x in ar3:
    for y in x:
        for z in y:
            print(z)

'''
Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

Iterating on Each Scalar Element
In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
'''
# Iterate through the following 3-D array
arF = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arF.shape)
for x in np.nditer(arF):
    print(x)
'''
Iterating Array With Different Data Types
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']
'''

for x in np.nditer(arF, flags=['buffered'], op_dtypes="S"):
    print(x)

'''
Iterating With Different Step Size
We can use filtering and followed by iteration.

Example
Iterate through every scalar element of the 2D array skipping 1 element:
'''
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)
'''
Enumerated Iteration Using ndenumerate()
Enumeration means mentioning sequence number of somethings one by one.

Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
'''
# Enumerate on following 1D arrays elements:

ar1d = np.array([1, 2, 3, 4])

for idx, x in np.ndenumerate(ar1d):
    print(idx, x)

# Enumerate on following 2D array's elements:

ar2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(ar2d):
    print(idx, x)
