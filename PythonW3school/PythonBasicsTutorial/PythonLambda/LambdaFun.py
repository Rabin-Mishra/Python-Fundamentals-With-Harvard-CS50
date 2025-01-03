'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:
'''

# Multiply argument a with argument b and return the result:


def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))

'''
Use that function definition to make a function that always doubles the number you send in:
'''


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
