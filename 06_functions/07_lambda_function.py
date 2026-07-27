"""
=========================================================
Topic       : Lambda Function
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Lambda Function
# ----------------------------------------

square = lambda x: x * x

print("Square :", square(5))

print()

# ----------------------------------------
# Addition Using Lambda
# ----------------------------------------

add = lambda a, b: a + b

print("Addition :", add(10, 20))

print()

# ----------------------------------------
# Maximum of Two Numbers
# ----------------------------------------

maximum = lambda a, b: a if a > b else b

print("Maximum :", maximum(25, 15))

print()

# ----------------------------------------
# Even or Odd
# ----------------------------------------

check = lambda n: "Even" if n % 2 == 0 else "Odd"

print("12 is", check(12))
print("15 is", check(15))

print()

# ----------------------------------------
# Lambda with sorted()
# ----------------------------------------

students = [
    ("Manas", 85),
    ("Rahul", 72),
    ("Aman", 91)
]

sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted by Marks:")
for student in sorted_students:
    print(student)
