# there are 3 numeric types in python
'''
int 
float 
complex
'''
# concept of type conversion
import random
a = 1
b = 1.5
c = '1j'
# conversion in between the values
p = float(a)
q = int(b)
r = complex(c)

print(a)
print(b)
print(c)
print('')
print(p)
print(q)
print(r)

'''
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
'''


print(random.randrange(1, 10))
