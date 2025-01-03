'''
Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
'''
x = -1

if x < 0:
    raise Exception("Sorry no numbers below zero")

y = "Hello"
if not type(y) is int:
    raise TypeError("Only integers allowed")
    
