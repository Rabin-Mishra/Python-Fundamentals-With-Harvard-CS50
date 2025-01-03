
"""
# wap to check if a number is positive
a = 10
if a > 0:
    print("The number is positive")

print(f"The number is {a}")
"""

"""
# wap to check whether a number is odd or even
a = 10
if a % 2 == 0:
    print(f"The number is even and it is {a}")
else:
    print(f"The number is odd and it is {a}")
"""


"""
# wap to create an area 0f rectangle
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
area = length*breadth
print(f"The obtainede area from the area of rectangle is {area}")
"""


"""

# wap to check whether the passed letter is vowel or not
vowels = ['a', 'e', 'i', 'o', 'u']
passedLetter = input("Enter a letter: ")
print(passedLetter.lower() in vowels)
if passedLetter.lower() in vowels:
    print(f"It is a vowel\n Passed Letter= {passedLetter} ")
else:
    print(f"Passed letter is a consonant and it is {passedLetter}")
"""

# wAP  to check if a number is single digit number 2-digit number and so on upto 5 digits


def check_number_type(num):
    if num < 0:
        return "Negative numbers are not allowed"
    elif num < 10:
        return "Single-digit number"
    elif num < 100:
        return "Two-digit number"
    elif num < 1000:
        return "Three-digit number"
    elif num < 10000:
        return "Four-digit number"
    elif num < 100000:
        return "Five-digit number"
    else:
        return "Number has more than five digits"


# Test the function
num = int(input("Enter a number: "))
print(check_number_type(num))
