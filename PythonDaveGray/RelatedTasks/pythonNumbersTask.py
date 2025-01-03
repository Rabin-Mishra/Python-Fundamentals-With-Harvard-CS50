'''
Task Description:
Write a Python program that generates a random mathematical expression involving all three numeric types (int, float, complex). Then, perform type conversion on each variable, and print both the original values and the converted values.
'''

import random
# generate a random values for a,b and c

a = random.randint(1, 10)
b = random.uniform(1, 10)
c = complex(0, random.randint(1, 10))

expression = a + b - (c.real * b) / a + c.imag

# perform the type conversion

p = float(a)
q = int(b)
r = int(c.real)

# Print the original and converted values
print("Original Values:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}\n")

print("Converted Values:")
print(f"p = {p}")
print(f"q = {q}")
print(f"r = {r}")

# Print the result of the expression
print("\nResult of the Expression:")
print(f"Expression = {expression}")
