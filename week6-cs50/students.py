import csv


students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
#    reader = csv.reader(file)
    for row in reader:
        students.append(row)

#    for line in file:
#        name, home = line.rstrip().split(",")
#        student = {"name": name, "house": home}
#        students.append(student)


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")