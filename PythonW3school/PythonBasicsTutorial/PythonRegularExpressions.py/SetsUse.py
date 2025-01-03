import re

# Example string
text = "hello world 123"

# Match any 'a', 'r', or 'n'
print(re.findall("[arn]", text))  # Output: ['r']

# Match any lowercase character from 'a' to 'n'
print(re.findall("[a-n]", text))  # Output: ['h', 'e', 'l', 'l', 'o', 'l', 'o']

# Match any character except 'a', 'r', or 'n'
# Output: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'l', 'd', ' ', '1', '2', '3']
print(re.findall("[^arn]", text))

# Match any digit from '0' to '9'
print(re.findall("[0-9]", text))  # Output: ['1', '2', '3']

# Match any two-digit number from '00' to '59'
print(re.findall("[0-5][0-9]", text))  # Output: ['12']

# Match any alphabetic character, either lowercase or uppercase
# Output: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
print(re.findall("[a-zA-Z]", text))
