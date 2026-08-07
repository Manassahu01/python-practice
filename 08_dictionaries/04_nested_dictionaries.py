"""
=========================================================
Topic       : Nested Dictionaries
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a Nested Dictionary
# ----------------------------------------

students = {
    "student1": {
        "name": "Manas",
        "age": 20,
        "course": "BCA"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "B.Tech"
    }
}

print("Nested Dictionary:")
print(students)

print()

# ----------------------------------------
# Access Nested Dictionary Values
# ----------------------------------------

print("Student 1 Name :", students["student1"]["name"])
print("Student 2 Course :", students["student2"]["course"])

print()

# ----------------------------------------
# Modify Nested Dictionary
# ----------------------------------------

students["student1"]["age"] = 21

print("After Updating Age:")
print(students["student1"])

print()

# ----------------------------------------
# Add New Data
# ----------------------------------------

students["student1"]["city"] = "Bhilai"

print("After Adding City:")
print(students["student1"])

print()

# ----------------------------------------
# Add New Student
# ----------------------------------------

students["student3"] = {
    "name": "Aman",
    "age": 22,
    "course": "MCA"
}

print("After Adding Student 3:")
print(students)

print()

# ----------------------------------------
# Employee Example
# ----------------------------------------

employees = {
    "E101": {
        "name": "Ankit",
        "department": "IT"
    },
    "E102": {
        "name": "Priya",
        "department": "HR"
    }
}

print("Employees:")
print(employees)

print()

print("Employee E101 Name :", employees["E101"]["name"])
print("Employee E102 Department :", employees["E102"]["department"])
