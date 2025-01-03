import re

txt = "The rain in Spain"

x = re.findall("ai", txt)
print(x)
# Return an empty list if no match was found:
y = re.findall("Portugal", txt)
print(y)

'''
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:
'''
txt = "The rain in Spain"
a = re.search("\s", txt)

print("The first white-space character is located in position:", a.start())

'''
The split() Function
The split() function returns a list where the string has been split at each match:

'''

txt1 = "The rain in Spain"
b = re.split("\s", txt1)
print(b)
'''
The sub() Function
The sub() function replaces the matches with the text of your choice:

Example
Replace every white-space character with the number 9:
'''

txt2 = "The rain in Spain"
c = re.sub("\s", "9", txt2)
print(c)

'''
Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.
'''
txt4 = "The rain in Spain"
d = re.search("ai", txt)
print(txt4)
'''
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''
# Example
# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# printing the string passed into a function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# printing a part of the string where there was a match
# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
