import json

# Python objects
python_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
python_list = [1, 2, 3, 4, 5]
python_tuple = (1, 2, 3, 4, 5)
python_str = 'Hello, World!'
python_int = 42
python_float = 3.14
python_bool_true = True
python_bool_false = False
python_none = None

# Convert Python objects to JSON equivalents
json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_tuple = json.dumps(python_tuple)
json_str = json.dumps(python_str)
json_int = json.dumps(python_int)
json_float = json.dumps(python_float)
json_bool_true = json.dumps(python_bool_true)
json_bool_false = json.dumps(python_bool_false)
json_none = json.dumps(python_none)

# Print the changes
print("Python Dictionary:", python_dict)
print("JSON Equivalent:", json_dict)

print("\nPython List:", python_list)
print("JSON Equivalent:", json_list)

print("\nPython Tuple:", python_tuple)
print("JSON Equivalent:", json_tuple)

print("\nPython String:", python_str)
print("JSON Equivalent:", json_str)

print("\nPython Integer:", python_int)
print("JSON Equivalent:", json_int)

print("\nPython Float:", python_float)
print("JSON Equivalent:", json_float)

print("\nPython True:", python_bool_true)
print("JSON Equivalent:", json_bool_true)

print("\nPython False:", python_bool_false)
print("JSON Equivalent:", json_bool_false)

print("\nPython None:", python_none)
print("JSON Equivalent:", json_none)
