# Example
# Convert a Python object containing all the legal data types:

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# we can also use the indent parameter to define the number of indents  to format the result
print(json.dumps(x, indent=4))
'''
You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
'''
# sort the result alphabetically by keys or order them
# Use the separators parameter to change the default separator
print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))
