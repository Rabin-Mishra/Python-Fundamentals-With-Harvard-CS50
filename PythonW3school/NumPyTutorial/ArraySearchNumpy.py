'''
NumPy Searching Arrays
Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method.
'''
# Find the indexes where the value is 4:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 6, 4, 7, 4])
print("The array contains the values as \n", arr)
x = np.where(arr == 4)
print("The indexes where the number 4 in the array exists are \n", x)

# for the same array finding the values of the indexes where the values are even

y = np.where(arr % 2 == 0)
print("The indexes where the array is even is \n", y)

# similarly finding the indexes where the values are odd
z = np.where(arr % 2 == 1)
print("The indexes on which the array values are odd are \n", z)

'''
Search Sorted
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.
'''

ar1 = np.array([6, 7, 8, 9])
searchVal = np.searchsorted(ar1, 7)
'''
Example explained: The number 7 should be inserted on index 1 to remain the sort order.

The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
'''
print("The indexes at which the sorted values searched resides are:\n", searchVal)

# we can also do the searching from the right side for that we must give side='right ' to return the right most index instead

searchRight = np.searchsorted(ar1, 7, side='right')
print('The index at which the value lies searched from the right is \n', searchRight)
