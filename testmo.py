import csv

names = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for name, home in reader: 

for student in sorted(names, key= lambda student: student["name"], reverse= True):
    print(f"{student['name']} {student['home']}")