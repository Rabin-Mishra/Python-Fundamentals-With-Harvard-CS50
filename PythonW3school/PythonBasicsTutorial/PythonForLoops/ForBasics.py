# ExampleGet your own Python Server
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

# use of brek statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# use of continue keyword to skip the particular value in the list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

'''
The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

Example
Increment the sequence with 3 (default is 1):
'''
for x in range(2, 30, 3):
    print(x)


'''Nested Loops concepts'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
