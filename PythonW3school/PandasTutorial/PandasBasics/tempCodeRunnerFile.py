'''
Pandas DataFrames
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''

import pandas as pd
data = {
    'calories': [420, 200, 300]
    'time': [50, 10, 20]
}
# load the data into dataframe object
df = pd.DataFrame(data)
print(df)
