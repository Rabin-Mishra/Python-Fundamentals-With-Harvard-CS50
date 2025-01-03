current_year = 2023

name = 'Rabin'
age = 19
# use of the concept of formatted string
print(f"{name} is {age} years old at the current year{current_year}")

'''Create a function calculate_birth_year that takes the current year and age as parameters and calculates the birth year. The function should return the birth year.
'''


def calculate_birth_year(current_year, age):
    birth_year = current_year-age
    return birth_year


birth_year = calculate_birth_year(current_year, age)

print(f"{name}'s birth year is {birth_year}.")

favorite_fruits = ['apple', 'mango', 'banana']
# unpack the list into 3 variables
x, y, z = favorite_fruits
print(x, y, z)

global_variable = 22


def local_function():
    local_variable = 23
    global global_variable
    global_variable = 25
    print(f"The global variable is {global_variable}")
    print(f"The local variable is {local_variable}")


local_function()
print(f"The modified value is{global_variable}")
'''
Task: Working with Variables and Functions

Create a variable current_year and assign it the current year.
Create variables name and age and assign them values.
Print a statement using a formatted string to display the name, age, and the current year.
Create a function calculate_birth_year that takes the current year and age as parameters and calculates the birth year. The function should return the birth year.
Call the calculate_birth_year function, passing the current_year and age as arguments, and store the result in a variable called birth_year.
Print a statement using a formatted string to display the calculated birth year.
Create a list favorite_fruits with at least three fruit names.
Unpack the list into three variables: fruit1, fruit2, and fruit3.
Print the unpacked variables.
Create a global variable global_variable and assign it a value.
Create a function local_function that prints the global variable.
Call the local_function to demonstrate accessing the global variable inside the function.
Create a local variable local_variable within the function local_function and print it.
Use the global keyword to modify the value of global_variable inside local_function.
Print the modified value of global_variable outside the function.
'''
