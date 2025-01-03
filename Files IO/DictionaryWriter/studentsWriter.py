import csv

name = input("What's your name?")
home = input("Where's  your home?")

with open("studentsWriter.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

with open("studentsWriter2.csv", "a") as file2:
    writer = csv.DictWriter(file2,fieldnames=['name','home'])
    writer.writerow({"name": name, "home": home})
