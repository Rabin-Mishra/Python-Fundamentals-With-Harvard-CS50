def my_function():
    print("Hello from a function")


my_function()
'''
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
'''


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")

'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''


def my_fun(*kids):
    print("The Youngest child is "+kids[2])


my_fun("Rabin", "Nabin", "Sabin")

'''
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
'''


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


'''
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# use of parameters in the functions


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# passing of a list as an argument


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# returning a value in function using return keyword


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

'''
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
'''
def my_function(x, /):
  print(x)

my_function(3)
