with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")

print('')
with open("students.csv") as file1:
    for line1 in file1:
        name, place = line1.rstrip().split(",")
        print(f"{name} lives in {place}")
