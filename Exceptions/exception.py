try:
    x = int(input("Whats x?"))
except ValueError:
    print("X is not an integer")
else:
    print(f"The value of x is {x}")
