"""
=========================================================
Topic       : Nested Lists
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a Nested List
# ----------------------------------------

students = [
    ["Manas", 85],
    ["Rahul", 78],
    ["Aman", 92]
]

print("Nested List:")
print(students)

print()

# ----------------------------------------
# Access Elements
# ----------------------------------------

print("First Student :", students[0])
print("First Student Name :", students[0][0])
print("First Student Marks :", students[0][1])

print()

# ----------------------------------------
# Access Second Row
# ----------------------------------------

print("Second Student :", students[1])
print("Name :", students[1][0])
print("Marks :", students[1][1])

print()

# ----------------------------------------
# Modify Nested List
# ----------------------------------------

print("Before :", students)

students[2][1] = 95

print("After  :", students)

print()

# ----------------------------------------
# Iterate Through Nested List
# ----------------------------------------

for student in students:
    print(student)

print()

# ----------------------------------------
# Matrix Example
# ----------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print()

# ----------------------------------------
# Access Matrix Elements
# ----------------------------------------

print("matrix[0][0] =", matrix[0][0])
print("matrix[1][2] =", matrix[1][2])
print("matrix[2][1] =", matrix[2][1])
