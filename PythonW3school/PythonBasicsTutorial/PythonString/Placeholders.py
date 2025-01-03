'''
You can perform if...else statements inside the placeholders:

Example
Return "Expensive" if the price is over 50, otherwise return "Cheap":
'''
price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)


'''
The function does not have to be a built-in Python method, you can create your own functions and use them:

Example
Create a function that converts feet into meter
'''
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

'''
More Modifiers
At the beginning of this chapter we explained how to use the .2f modifier to format a number into a fixed point number with 2 decimals.

There are several other modifiers that can be used to format values:
'''
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)