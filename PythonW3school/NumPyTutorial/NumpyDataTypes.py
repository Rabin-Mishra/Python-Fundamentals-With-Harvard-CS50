'''
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
# Checking the Data Type of an Array
# The NumPy array object has a property called dtype that returns the data type of the array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# use of dtype property to return the datatype of array

print(arr.dtype)
print(arr)

arS = np.array(['apple', 'banana', 'cherry', 'berry'])

print(arS.dtype)
print(arS)

'''
Creating Arrays With a Defined Data Type
We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
'''

arD = np.array([1, 2, 3, 4, 5, 6], dtype='S')
print(arD)
print(arD.dtype)

# For i, u, f, S and U we can define size as well.

# Example
# Create an array with data type 4 bytes integer:

arE = np.array([1, 2, 3, 4], dtype='i4')
print(arE)
print(arE.dtype)
'''
Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
'''
# change datatype from float to integer by using 'i'
# as parameter value

arF = np.array([1.2, 2.2, 3.2])

newArr = arF.astype('i')

print(newArr)
print(newArr.dtype)

# changing datatype from integer to boolean
arI = np.array([1, 2, 3, 4, 5, 6, 7])

newBool = arI.astype(bool)

print(newBool)
print(newBool.astype)
