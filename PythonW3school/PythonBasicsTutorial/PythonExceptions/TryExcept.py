'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:
'''
# The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print('An eror encountered')


try:
    print(y)
except NameError:
    print("Variable y is not defined")
except:
    print("Some other sort of error")

'''
Else
You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:
'''
try:
    print("Hello")
except:
    print("Sth went Worng")
else:
    print('Nth went wrong')

    '''
    The finally block, if specified, will be executed regardless if the try block raises an error or not.
    '''
try:
    print(x)
except:
    print("Sth went Wrong")
finally:
    print("The try except is finished")
