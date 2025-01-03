'''
Splitting NumPy Arrays
Splitting is reverse operation of Joining.

Joining merges multiple arrays into one and Splitting breaks one array into multiple.

We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
'''
# split the array in 3 parts

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])

newArr = np.array_split(arr, 3)
print('Splitting the array in 3 parts', newArr)
# If the array has less elements than required, it will adjust from the end accordingly.
print('Splitting the array in 4 parts', np.array_split(arr, 4))

'''
Split Into Arrays
The return value of the array_split() method is an array containing each of the split as an array.

If you split an array into 3 arrays, you can access them from the result just like any array element
'''
# Example
# Access the splitted arrays:
print(f"Obtainig splitted arrays 1st is ", newArr[0])
print(f"Obtainig splitted arrays 2nd is ", newArr[1])
print(f"Obtainig splitted arrays 3rd is ", newArr[2])

'''
Splitting 2-D Arrays
Use the same syntax when splitting 2-D arrays.

Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
'''
# Split the 2-D array into three 2-D arrays.

ar2D = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
ar2DSplit = np.array_split(ar2D, 3)
print("The splitted 2d array is  ", ar2DSplit)
'''
The example above returns three 2-D arrays.

Let's look at another example, this time each element in the 2-D arrays contains 3 elements.

Example
Split the 2-D array into three 2-D arrays.
'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
               10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)

'''
The example above returns three 2-D arrays.

In addition, you can specify which axis you want to do the split around.

The example below also returns three 2-D arrays, but they are split along the row (axis=1).
'''
# Split the 2-D array into three 2-D arrays along rows.

newArrRow = np.array_split(arr, 3, axis=1)
print("The array along the row using axis =1 is ", newArrRow)
