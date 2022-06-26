#!/usr/bin/env python3


def new_function(members, students):
	print("This is a function")

	for member in members:
		if member['age'] <= 18:
			students.append({"name": member['name'], "title": member['title'], "age": member['age'], "minor": True})


new_function(members=[{"name": "test"}], students=[])
