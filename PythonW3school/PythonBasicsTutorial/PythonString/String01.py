'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

Before Python 3.6 we had to use the format() method.
'''
'''
F-Strings
F-string allows you to format selected parts of a string.

To specify a string as an f-string, simply put an f in front of the string literal, like this:
'''

txt = f"Hi this is Rabin"
print(txt)

price = 10
text = f"The price is {price} dollars"
print(text)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
