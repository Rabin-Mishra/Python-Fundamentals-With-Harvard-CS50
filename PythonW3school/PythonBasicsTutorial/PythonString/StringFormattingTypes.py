'''
Here is a list of all the formatting types.

Formatting Types
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
'''

value = 12345.6789

# Left aligns the result (within the available space)
print(f'{value:<20}')  

# Right aligns the result (within the available space)
print(f'{value:>20}')  

# Center aligns the result (within the available space)
print(f'{value:^20}')  

# Places the sign to the left most position
print(f'{value:=+20}')  

# Use a plus sign to indicate if the result is positive or negative
print(f'{value:+20}')  

# Use a minus sign for negative values only
print(f'{value:-20}')  

# Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
print(f'{value: 20}')  

# Use a comma as a thousand separator
print(f'{value:,}')  

# Use a underscore as a thousand separator
print(f'{value:_}')  

# Binary format
print(f'{value:b}')  

# Converts the value into the corresponding Unicode character
print(f'{value:c}')  

# Decimal format
print(f'{value:d}')  

# Scientific format, with a lower case e
print(f'{value:e}')  

# Scientific format, with an upper case E
print(f'{value:E}')  

# Fix point number format
print(f'{value:f}')  

# Fix point number format, in uppercase format (show inf and nan as INF and NAN)
print(f'{value:F}')  

# General format
print(f'{value:g}')  

# General format (using a upper case E for scientific notations)
print(f'{value:G}')  

# Octal format
print(f'{value:o}')  

# Hex format, lower case
print(f'{value:x}')  

# Hex format, upper case
print(f'{value:X}')  

# Number format
print(f'{value:n}')  

# Percentage format
print(f'{value:%}')  
