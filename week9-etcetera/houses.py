"""
Sets do not allow repeated elements by default. They are unordered too. 
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

#houses = []
houses = set()
for student in students:
    #if student["house"] not in houses:
    houses.add(student["house"])

print(houses) # print in random order
for house in sorted(houses):
    print(house)