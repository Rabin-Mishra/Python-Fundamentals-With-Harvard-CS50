import csv
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": name, "place": place})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives in {student['place']}")
