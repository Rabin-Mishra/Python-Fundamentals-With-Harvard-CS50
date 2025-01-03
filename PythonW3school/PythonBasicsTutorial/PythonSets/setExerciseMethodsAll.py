# add()
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# clear()
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# copy()
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

# difference()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference = set1.difference(set2)
print(difference)  # Output: {1}

# difference_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}

# discard()
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

# intersection()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1.intersection(set2)
print(intersection)  # Output: {2, 3}

# intersection_update()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}

# isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

# issubset()
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True

# <
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1 < set2)  # Output: True

# issuperset()
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True

# >
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1 > set2)  # Output: True

# pop()
my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: 1 (Note: Since sets are unordered, any element can be popped)
print(my_set)   # Output: {2, 3}

# remove()
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# symmetric_difference()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # Output: {1, 4}
