'''
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3U = set1.union(set2)
print(set3U)
# also can use the | operator to get the same result as that of union
set3UO = set1 | set2
print(set3UO)

# for adding more than one set
set1a = {"a", "b", "c"}
set2a = {1, 2, 3}
set3a = {"John", "Elena"}
set4a = {"apple", "bananas", "cherry"}

myset = set1a.union(set2a, set3a, set4a)
print(myset)
# use of the or operator for the same thing
mysetO = set1a | set2a | set3a | set4a
print(mysetO)

# join of set and a tuple using union()
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1I = {"apple", "banana", "cherry"}
set2I = {"google", "microsoft", "apple"}

set3 = set1I.intersection(set2I)
print(set3)
set3A = set1I & set2I
print(set3A)

# intersection_update()
set1I.intersection_update(set2I)
print(set1I)
# difference
setD = set1.difference(set2)
print(setD)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
