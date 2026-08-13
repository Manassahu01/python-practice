"""
=========================================================
Topic       : Nested Tuples
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Create a Nested Tuple
students = (
    ("Manas", 85),
    ("Rahul", 78),
    ("Aman", 92)
)

print("Nested Tuple:")
print(students)
print()

# Access Nested Tuple Elements
print("First Student :", students[0])
print("First Student Name :", students[0][0])
print("First Student Marks :", students[0][1])
print()

# Access Other Students
print("Second Student Name :", students[1][0])
print("Second Student Marks :", students[1][1])
print("Third Student Name :", students[2][0])
print("Third Student Marks :", students[2][1])
print()

# Nested Tuple with Different Data
data = (
    ("Python", 100),
    ("NumPy", 90),
    ("Pandas", 85)
)

print("Course Data:")
print(data)
print()

print("Course :", data[0][0])
print("Score  :", data[0][1])
print()

# Matrix using Nested Tuple
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")
for row in matrix:
    print(row)

print()

# Access Matrix Elements
print("matrix[0][0] :", matrix[0][0])
print("matrix[1][2] :", matrix[1][2])
print("matrix[2][1] :", matrix[2][1])
