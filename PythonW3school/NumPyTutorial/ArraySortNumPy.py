'''
Sorting Arrays
Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified
'''
import numpy as np
arr = np.array([1, 2, 5, 8, 9, 0, 2, 8])
print("The original unordered array has the values as \n", arr)

arrSort = np.sort(arr)
print('The sorted array obtained using the sort() method is \n', arrSort)
# Note: This method returns a copy of the array, leaving the original array unchanged.

# sorting the array alphabetically
ar1 = np.array(['banana', 'cherry', 'apple', 'rabin', 'sabin'])
print("The original array input was \n", ar1)
arSortAlpha = np.sort(ar1)
print("The alphabetically sorted array is \n", arSortAlpha)

# sorting a 2d array
ar2d = np.array([[1, 4, 7, 9], [3, 2, 5, 8]])
print("The unordered or unsorted array was \n", ar2d)
ar2dSort = np.sort(ar2d)
print("The sorted 2D array is \n", ar2dSort)
