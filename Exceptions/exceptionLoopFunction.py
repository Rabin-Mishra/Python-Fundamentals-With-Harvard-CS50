def main():
    x = get_int()
    print(f"The value of x is {x}")


def get_int():
    while True:
        try:
            return int(input("Whats x?"))
        except ValueError:
            print("X is not an integer")


main()
