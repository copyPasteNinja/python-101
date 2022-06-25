#!/usr/bin/env python3

members = [
    {"id": "01", "name": "Justin", "title": "student", "age": 20}, 
    {"id": "02", "name": "Uruj", "title": "student", "age": 13},
	{"id": "02", "name": "Abdul", "title": "instructor", "age": 21},
	{"id": "02", "name": "Zhapar", "title": "developer", "age": 21},
	{"id": "02", "name": "Kris", "title": "instructor", "age": 21},
	{"id": "02", "name": "Ahmad", "title": "instructor", "age": 31},
	{"id": "02", "name": "Danial", "title": "student", "age": 21}
]


students = []
for member in members:
	if member['age'] <= 18:
		students.append({"name": member['name'], "title": member['title'], "age": member['age'], "minor": True})	
			

print(students)