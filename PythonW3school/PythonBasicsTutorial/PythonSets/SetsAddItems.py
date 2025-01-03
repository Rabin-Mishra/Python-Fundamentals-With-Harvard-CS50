# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets
'''To add items from another set into the current set, use the update() method
'''
thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset1.update(tropical)

print(thisset1)

# adding of any of the iterable
set1 = {"apple", "orange", "Happy"}
list1 = ["Kiwi", "cherry"]

set1.update(list1)

print(set1)
