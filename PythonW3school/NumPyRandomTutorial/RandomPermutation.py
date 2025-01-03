'''
Random Permutations
Random Permutations of Elements
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation().

Shuffling Arrays
Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

'''
# randomly shuffle elements from the array
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("The original  array was\n", arr)
# The shuffle() method makes changes to the original array.
random.shuffle(arr)
print("The shuffled array is\n", arr)

# generating perrmutation of arrays
print("Random permutation of array is \n", random.permutation(arr))
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
