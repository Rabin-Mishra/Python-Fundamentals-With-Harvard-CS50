myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)
# Or, if you want to add three dictionaries into a new dictionary:

ch1 = {
    "name": "Emil",
    "year": 2004
}
ch2 = {
    "name": "Tobias",
    "year": 2007
}
ch3 = {
    "name": "Linus",
    "year": 2011
}

myFam = {
    "Child1a": ch1,
    "Child2a": ch2,
    "Child3a": ch3
}
print(myFam)

# Accessing the items in the list
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
