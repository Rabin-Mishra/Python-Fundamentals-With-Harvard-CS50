'''
Random Numbers in NumPy
What is a Random Number?
Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

Pseudo Random and True Random.
Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.

If there is a program to generate random number it can be predicted, thus it is not truly random.

Random numbers generated through a generation algorithm are called pseudo random.

Can we make truly random numbers?

Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.

We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).

In this tutorial we will be using pseudo random numbers.
'''
'''
Generate Random Number
NumPy offers the random module to work with random numbers.
'''
# Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print("Random int value is \t", x)
# for generating a random float value use rand()
# generating between 0 t0 1 no values inside rand() function
y = random.rand()
print("Random float value is \t", y)

'''
Generate Random Array
In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

Integers
The randint() method takes a size parameter where you can specify the shape of an array.
'''
# Generate a 1-D array containing 5 random integers from 0 to 100:

ar1d = random.randint(100, size=(5))
print("1D array containing random integers of 1 to 100 is \n", ar1d)
# generating a 2d array containing values from 0 to 100 with 3 rows each row with 5 random integers

ar2dint = random.randint(100, size=(3, 5))
print('the obtained 2d array with 3 rows and 5 columns in in each row is \n', ar2dint)
'''
The choice() method also allows you to return an array of values.

Add a size parameter to specify the shape of the array.
'''
# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

ar2d = random.choice([3, 5, 7, 9], size=(3, 5))
print(
    "The 2d array of order 3*5 with the random values from the set of passed array of numbers [3,5,7,9] is \n", ar2d)
