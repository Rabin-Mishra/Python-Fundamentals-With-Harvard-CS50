# clear()
my_dict = {"name": "John", "age": 30}
my_dict.clear()
print(my_dict)  # Output: {}

# copy()
my_dict = {"name": "John", "age": 30}
new_dict = my_dict.copy()
print(new_dict)  # Output: {"name": "John", "age": 30}

# fromkeys()
keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# get()
my_dict = {"name": "John", "age": 30}
value = my_dict.get("age")
print(value)  # Output: 30

# items()
my_dict = {"name": "John", "age": 30}
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 30)])

# keys()
my_dict = {"name": "John", "age": 30}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])

# pop()
my_dict = {"name": "John", "age": 30}
value = my_dict.pop("age")
print(value)  # Output: 30

# popitem()
my_dict = {"name": "John", "age": 30}
item = my_dict.popitem()
print(item)  # Output: ('age', 30)

# setdefault()
my_dict = {"name": "John"}
value = my_dict.setdefault("age", 30)
print(value)  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# update()
my_dict = {"name": "John"}
my_dict.update({"age": 30})
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# values()
my_dict = {"name": "John", "age": 30}
values = my_dict.values()
print(values)  # Output: dict_values(['John', 30])
