students = []
with open("students.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        students.append(f"{name} lives in {place}")

for student in sorted(students):
    print(student)
