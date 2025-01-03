'''
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
'''
# create a simple pandas series from a list
import pandas as pd
a = [1, 7, 2]
myVar = pd.Series(a)
print(myVar)

'''
Create Labels
With the index argument, you can name your own labels.
'''
# creating my own labels:
myVar = pd.Series(a, index=['x', 'y', 'z'])
print(myVar)

# referencing a item using a label
print(myVar['z'])


# creating a key/value object as Series
calCount = {'day1': 400, 'day2': 300, 'day3': 200}
myVar = pd.Series(calCount)
# the keys of the dictionary becomes the labels
print(myVar)
# for accessing dict items
myVar2 = pd.Series(calCount, index=['day1', 'day2'])
print(myVar2)

'''
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
'''
# Create a DataFrame from two Series
data = {
    'calCount': [400, 200, 300],
    'time': [50, 60, 70]
}
myVar3 = pd.DataFrame(data)
print(myVar3)
