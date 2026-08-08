"""
=========================================================
Topic       : Dictionary Traversal
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

student = {
    "name": "Manas",
    "age": 20,
    "course": "BCA",
    "city": "Bhilai"
}

print("Dictionary:")
print(student)
print()

# Traverse Dictionary Directly
print("Keys using for loop:")

for key in student:
    print(key)

print()

# Traverse using keys()
print("Using keys():")

for key in student.keys():
    print("Key :", key)

print()

# Traverse using values()
print("Using values():")

for value in student.values():
    print("Value :", value)

print()

# Traverse using items()
print("Using items():")

for key, value in student.items():
    print("Key :", key, "| Value :", value)

print()

# Nested Dictionary Traversal
students = {
    "student1": {
        "name": "Manas",
        "marks": 85
    },
    "student2": {
        "name": "Rahul",
        "marks": 78
    },
    "student3": {
        "name": "Aman",
        "marks": 92
    }
}

print("Nested Dictionary:")

for student_id, details in students.items():
    print("ID :", student_id)
    print("Name :", details["name"])
    print("Marks :", details["marks"])
    print("-" * 20)
