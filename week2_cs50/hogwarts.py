students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=', ')

#students = {
#    "Hermione": "Griffindor", 
#    "Harry": "Griffindor",
#    "Ron": "Grinffindor",
#    "Draco": "Slytherin",
#}

#for student in students:
#    print(f"Student: {student} | House: {students[student]}")

#students = ["Hermione", "Harry", "Ron"]
#houses = ["Griffindor", "Slytherin"]

#for i in range(len(students)):
#    print(f"student {i+1}: {students[i]}")