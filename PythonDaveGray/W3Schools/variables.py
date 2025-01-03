# creating variables in python
x = 5
y = 'Rabin'
print(x)
print(y)

# casating of a variables
a = str(3)
b = int(3)
c = float(3)
print(a)
print(b)
print(c)

# getting the type of a variabels
print(type(a))
print(type(b))
print(type(c))

# use of camelCase,PascalCase and snake_case is used for the variable declaration
# assigning multiple values at the same time
fruit1, fruit2, fruit3 = "apple", "banana", "cherry"
print('\n', "Fruits are: ", fruit1, "\n", fruit2, "\n", fruit3, '\n')
# assigning one values to multiple variables

f1 = f2 = f3 = 'apple'
print(f1)
print(f2)
print(f3, '\n')

# unpacking a collection of varibles in python collection given in list or tuples

fruits = ['apple', 'orange', 'mango']
p, q, r = fruits
print(p)
print(q)
print(r, '\n')

# outputting multiple variabels in python

a = 'Python '
b = 'is '
c = 'awesome'
print(a, b, c, '\n')
print(a + b + c, '\n')

# use of global and local variable in python
# Create a variable outside of a function, and use it inside the function

var1 = 'Fantastico'


def myFunction():
    print('Python is '+var1)


myFunction()

'''If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.'''

var2 = 'Awesome'


def myFunc():
    x = 'Fantastic'
    print("Python is "+x)


myFunc()

print("Python is " + var2)

# use of global keyword to make the variable in the global scope


def myfun1():
    global val1
    val1 = 'Gloabal variable'


myfun1()

print("extracting from the locally declared global variable"+val1)

# also if you want to change the value of global varible inside the function use the keyword global

jay = 'sambho'


def funnn():
    global jay
    jay = 'Har Har mahadev'

    print(jay)


funnn()
print(jay)
