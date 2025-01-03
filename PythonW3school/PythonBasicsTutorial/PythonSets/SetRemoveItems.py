'''
To remove the items in set we will be using the remove() and discard() functions wherein if the item to be removed is not present in the set the remove() method will give an error while the discard() method wont
'''
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset1 = {"apple", "banana", "cherry"}

thisset1.discard("banana")

print(thisset1)

# use of the pop method to remove items
thissetp = {"apple", "banana", "cherry"}

x = thissetp.pop()

print(x)

print(thissetp)

# use of the clear() method
thissetC = {"apple", "banana", "cherry"}

thissetC.clear()

print(thissetC)

#use of the del keyword
thissetD = {"apple", "banana", "cherry"}

del thissetD

print(thissetD)