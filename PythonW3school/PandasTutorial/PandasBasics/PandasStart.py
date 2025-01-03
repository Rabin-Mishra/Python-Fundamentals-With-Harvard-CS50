import pandas as pd

myDSet = {
    'cars': ['BMW', 'Volvo', 'Nissan'],
    'passings': [3, 7, 2]
}
myVar = pd.DataFrame(myDSet)
print(myVar)
