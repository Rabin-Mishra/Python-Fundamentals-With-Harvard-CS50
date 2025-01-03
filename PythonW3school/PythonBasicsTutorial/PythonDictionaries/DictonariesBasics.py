'''
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:

Dictionary Length
To determine how many items a dictionary has, use the len() function:

Dictionary Items - Data Types
The values in dictionary items can be of any data type:

type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.
'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "blue", "black"],
    "year": 2020
}
print(thisdict)
print(thisdict["brand"])
print(type(thisdict))
print(len(thisdict))

# creating a dictionary using a dict() constructor
dict1 = dict(name="Rabin", age=20, country="Nepal")
print(dict1)
# accessing items
print(thisdict["brand"])
print(thisdict.get("model"))
# getting the keys using the keys() method
print(thisdict.keys())

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the chang

# returning the values in the dictionary using the values() method or the function

print('\n', thisdict.values())

# use of items() function which will return all the items in the list as a tuples
print(thisdict.items())

# check if it exists in the dictionary
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# removing the items from the list
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)
'''
# clearing the dictonary using clear() method
thisdict.clear()
print(thisdict)
'''

# example of loops in the dictionary
for x, y in thisdict.items():
    print(x, y)
