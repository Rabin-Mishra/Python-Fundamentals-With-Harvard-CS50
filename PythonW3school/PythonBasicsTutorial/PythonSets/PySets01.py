thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
# duplicates
thisset1 = {"apple", "banana", "cherry", "apple"}

print(thisset1)

# True and 1 is considered the same value:

thisset2 = {"apple", "banana", "cherry", True, 1, 2}

print(thisset2)

# False and 0 is considered the same value:

thisset3 = {"apple", "banana", "cherry", False, True, 0}

print(thisset3)
