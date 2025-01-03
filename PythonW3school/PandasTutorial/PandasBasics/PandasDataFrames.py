'''
Pandas DataFrames
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''

import pandas as pd
data = {
    'calories': [420, 200, 300],
    'time': [50, 10, 20]
}
# load the data into dataframe object
df = pd.DataFrame(data)
print(df)
'''
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)
'''

print(df.loc[0])
# use a list of indexes
print(df.loc[[0, 1]])

# we can also name our own indexes
df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)
