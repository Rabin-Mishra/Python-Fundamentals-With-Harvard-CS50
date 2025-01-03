import re

# Example strings
strings = ["hello", "heo", "heoo", "planet", "heello", "heyo", "heeyo"]

# Regular expressions using metacharacters
patterns = [
    r"he.*o",    # Zero or more occurrences of any character between 'he' and 'o'
    r"he.+o",    # One or more occurrences of any character between 'he' and 'o'
    r"he.?o",    # Zero or one occurrence of any character between 'he' and 'o'
    r"^hello",   # Starts with 'hello'
    r"planet$",  # Ends with 'planet'
    r"he.{2}o",  # Exactly 2 occurrences of any character between 'he' and 'o'
    r"he(yo|llo)"  # Either 'hello' or 'heyo'
]

# Apply regular expressions to example strings
for pattern in patterns:
    print("Pattern:", pattern)
    for string in strings:
        if re.match(pattern, string):
            print(f"'{string}' matches the pattern")
    print()
