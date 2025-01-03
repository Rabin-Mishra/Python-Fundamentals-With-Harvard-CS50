while True:
    try:
        x = int(input("Whats x?"))
    except ValueError:
        print("X is not an integer")
    else:
        break
print(f"The value of x is {x}")
