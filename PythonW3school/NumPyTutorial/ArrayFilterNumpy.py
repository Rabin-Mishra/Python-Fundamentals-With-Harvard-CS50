'''
NumPy Filter Array
Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
'''
# Create an array from the elements on index 0 and 2:
import numpy as np
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newArr = arr[x]
print("The original array before filtering was \n", arr)

print("The new array obtained after filtering is \n", newArr)
'''
The example above will return [41, 43], why?

Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.
'''
'''
Creating the Filter Array
In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.
'''
# Create a filter array that will return only values higher than 42:

arF = np.array([41, 42, 43, 44, 45, 39, 43, 89])

# create an empty list
filter_arF = []

# go through each element in array

for element in arF:
    if element > 42:
        filter_arF.append(True)
    else:
        filter_arF.append(False)

newArF = arF[filter_arF]
print('The original content of values in the array to be filtered is \n', arF)
print("The value obtained at the filtered empty array or list is \n", filter_arF)
print('The obtained new array after filtering is ', newArF)

# for the same array filtering for just the even elements
# creating a new empty even list
even_filter = []
for evenCheck in arF:
    if evenCheck % 2 == 0:
        even_filter.append(True)
    else:
        even_filter.append(False)

newEvenArr = arF[even_filter]
print("The value inside of the original array unfiltered is \n", arF)
print("The even filtered array with its boolean representation is \n", even_filter)
print("The obtained array after filtering is \n", newEvenArr)

# for the same work we can commence it in different way as
'''
Creating Filter Directly From Array
The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.
'''

ar1 = np.array([41, 14, 42, 43, 44, 45])
filter_ar1 = ar1 > 42

ar1_filter = ar1[filter_ar1]
print('The original content of array was \n', ar1)
print("The boolean values for filtering obtained is \n", filter_ar1)
print("The filterd array contain as per the requirement is \n ", ar1_filter)

# using the same concept for directly creating the array for even elements

ar1_even = ar1 % 2 == 0
ar1_filter_even = ar1[ar1_even]
print("The content of the original array was \n", ar1)
print("The boolean terms obtained based on the filter condition for the even number is \n", ar1_even)
print("The obtained arrray filtered is \n", ar1_filter_even)
