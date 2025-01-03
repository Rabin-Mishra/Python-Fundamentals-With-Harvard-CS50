"""
Types of Operators:
1)Arithmetic Operators =(+,-,*,/,//,**,%)
2)Comparison Operators =(<,<=,!=,==,>=,>)
3)Logical Operators =(AND,OR,NOT)
4)Assignment Operators =(=,+=,-=,*=)
5)Identity Operators =(is,is not)
6)Membership Operators =(in ,not in )
7)Bitwise Operators =(&,|,^,<<,>>)

"""
# bitwise and

print(bin(14))
a = 10
b = 15
print(f"{a & b} also the binary is {bin(a & b)}")
print(a is b)

# bitwise or
a = 10
b = 15
print(f"{a | b} also the binary is {bin(a | b)}")
print(a is b)

# bitwise xor
a = 10
b = 15
print(f"{a ^ b} also the binary is {bin(a ^ b)}")
print(a is b)

# zero fill left shift
a = 10
b = 15
print(f"{a << 1} also the binary is {bin(a << b)}")
print(a is b)

print(bin(40))

text = "hello"
print("e" in text)
print("p" not in text)
print("e" not in text)
