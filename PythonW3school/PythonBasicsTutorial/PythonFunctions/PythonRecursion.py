
'''
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
'''


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
'''
Working of the above recursion
When tri_recursion(6) is called:

The function checks if 6 is greater than 0, which is true.
It calculates result = 6 + tri_recursion(5).
Inside the recursive call with k = 5:
It calculates result = 5 + tri_recursion(4).
Inside the recursive call with k = 4:
It calculates result = 4 + tri_recursion(3).
This process continues until k becomes 0.
As each recursive call returns, the intermediate results are printed.
The final result, which is the sum of integers from 6 down to 1, is returned and printed outside the function call.
'''
