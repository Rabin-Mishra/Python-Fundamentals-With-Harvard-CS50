import re

# Example strings
strings = ["The sun is shining.", "It's raining cats and dogs.",
           "I have 2 apples.", "Python is awesome!"]

# Regular expressions using special sequences
patterns = [
    r"\AThe",     # Returns a match if the string starts with 'The'
    r"\bain\b",   # Returns a match where 'ain' is a whole word
    r"\Bain\B",   # Returns a match where 'ain' is within a word, not at the beginning or end
    r"\d",        # Returns a match where the string contains digits
    r"\D",        # Returns a match where the string does not contain digits
    r"\s",        # Returns a match where the string contains whitespace
    r"\S",        # Returns a match where the string does not contain whitespace
    r"\w",        # Returns a match where the string contains word characters
    r"\W",        # Returns a match where the string does not contain word characters
    r"Spain\Z"    # Returns a match if the string ends with 'Spain'
]

# Apply regular expressions to example strings
for pattern in patterns:
    print("Pattern:", pattern)
    for string in strings:
        if re.search(pattern, string):
            print(f"'{string}' matches the pattern")
    print()
