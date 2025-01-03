i = 1
while i < 6:
    print(i)
    i += 1

# use of break statement
i = 1
while i < 6:
    print('\n', i)
    if i == 3:
        break
    i += 1
# use of continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# use of else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
