"""
=========================================================
Topic       : Accessing Dictionary Items
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a Dictionary
# ----------------------------------------

student = {
    "name": "Manas",
    "age": 20,
    "course": "BCA",
    "city": "Bhilai"
}

print("Student Dictionary:")
print(student)

print()

# ----------------------------------------
# Access Value using Key
# ----------------------------------------

print("Name   :", student["name"])
print("Course :", student["course"])

print()

# ----------------------------------------
# get() Method
# ----------------------------------------

print("Age   :", student.get("age"))
print("City  :", student.get("city"))
print("Phone :", student.get("phone", "Not Available"))

print()

# ----------------------------------------
# keys() Method
# ----------------------------------------

print(student.keys())

print()

# ----------------------------------------
# values() Method
# ----------------------------------------

print(student.values())

print()

# ----------------------------------------
# items() Method
# ----------------------------------------

print(student.items())

print()

# ----------------------------------------
# Check if Key Exists
# ----------------------------------------

if "name" in student:
    print("'name' key exists.")
else:
    print("'name' key does not exist.")

print()

# ----------------------------------------
# Update Dictionary Values
# ----------------------------------------

print("Before Update:")
print(student)

student["age"] = 21
student["course"] = "Data Science"

print("After Update:")
print(student)
