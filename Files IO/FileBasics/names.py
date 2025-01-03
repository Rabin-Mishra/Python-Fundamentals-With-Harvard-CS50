names = []
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

with open("names.txt", "a") as file:
    file.write(f"{names}\n")

with open("names.txt", 'r') as fileR:
    for line in fileR:
        names.append(line.rstrip())
    for name in sorted(names):
        print(f"Hello, {name}")

#if in case the file has not been closed properly but the concept of opening file in "with mode" generally does the work of closing the file itself
file.close()
fileR.close()