'''
Access Array Elements
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

'''
# accessing 1-D array
import numpy as np
ar1 = np.array([1, 2, 3, 4])
print(ar1[0])
print(ar1[1])
print(ar1[2])
print(ar1[3])

i = 0
for i in range(len(ar1)):
    print(ar1[i])

# getting multiple elements from the array
print(ar1[0]+ar1[3])

# accessing 2-d arrays
'''
Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.
'''
arr2 = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
print("2nd element on 1st row:", arr2[0, 1])

# access the element on 2nd row 4th column
print("4th element of 2nd row is :", arr2[1, 3])

# accessing 3d array
ar3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
'''
To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
'''
print(ar3[0, 1, 2])
'''
Example Explained
arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6
'''
'''
Negative Indexing
Use negative indexing to access an array from the end.

Example
Print the last element from the 2nd dim:
'''
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', arr[1, -1])
