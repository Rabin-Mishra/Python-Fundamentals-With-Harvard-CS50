'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.
'''

'''

Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.
The result will be a python dictionary
'''


# some JSON:
import json
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

'''
Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

'''
# generate a python object

a = {
    "name": "Rabin",
    "age": 20,
    "city": "Phidim"
}

# convert into JSON
b = json.dumps(a)

# the result is a JSON string
print(b)
'''
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
