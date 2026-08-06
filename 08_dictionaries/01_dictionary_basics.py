"""
=========================================================
Topic       : Dictionary Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Creating a Dictionary
# ----------------------------------------

student = {
    "name": "Manas",
    "age": 20,
    "course": "BCA"
}

print("Student Dictionary:")
print(student)

print()

# ----------------------------------------
# Dictionary with Different Data Types
# ----------------------------------------

data = {
    "integer": 10,
    "float": 10.5,
    "string": "Python",
    "boolean": True,
    "list": [1, 2, 3]
}

print(data)

print()

# ----------------------------------------
# Empty Dictionary
# ----------------------------------------

empty_dict = {}

print("Empty Dictionary :", empty_dict)

print()

# ----------------------------------------
# Creating Dictionary using dict()
# ----------------------------------------

employee = dict(id=101, name="Rahul", department="IT")

print(employee)

print()

# ----------------------------------------
# Duplicate Keys
# ----------------------------------------

person = {
    "name": "Aman",
    "name": "Manas",
    "age": 21
}

print(person)

print()

# ----------------------------------------
# Length of Dictionary
# ----------------------------------------

print("Length :", len(student))

print()

# ----------------------------------------
# Type of Dictionary
# ----------------------------------------

print("Type :", type(student))
