#use of tuple and concepts of tuple in python
'''
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(thistuple[1])



thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)
print(len(thistuple1))
print(thistuple1[2:5])

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

#Using the tuple() method to make a tuple:

thistupleP = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistupleP)
if "apple" in thistupleP:
  print("Yes apple is in this tuple")
