'''
String format()
Before Python 3.6 we used the format() method to format strings.

The format() method can still be used, but f-strings are faster and the preferred way to format strings.

The next examples in this page demonstrates how to format strings with the format() method.

The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:
'''
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# formatting for the multiple values
price = 12
itemno = 13
quantity = 3

myorder = 'I want {} pieces of item number {} for {:.2f} dollars'
print(myorder.format(quantity, itemno, price))


# use of indexing to format the string
'''
Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
'''
quantity = 4
itemno = 555
price = 23

myorder2 = 'I want {0} pieces of item number {1} for {2:.2f} dollars'

print(myorder2.format(quantity, itemno, price))

# use of index is prevalent if you want to use the same value for more than once
age = 22
name = "Rabin"

txt = "My name is {1}. I am {0} years old now you know my name is {1}"
print(txt.format(age, name))

'''
Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
'''
myorder3 = "I have a {carname}, it is a {model}."
print(myorder3.format(carname="Ford", model="Mustang"))
