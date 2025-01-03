students = []
with open("students.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        student = {"name": name, "place": place}
        students.append(student)


def get_name(student):
    return student["name"]


# it will actually be sorted with the names of in the reverse alphabetical order
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} lives in {student['place']}")
print('')
# here the code creates the function anonymously and allows to pass it the values
for student in sorted(students, key=lambda student: student["place"]):
    print(f"{student['name']} lives in {student['place']}")
