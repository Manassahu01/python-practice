"""
=========================================================
Topic       : Tuple Unpacking
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Basic Tuple Unpacking
# ----------------------------------------

student = ("Manas", 20, "BCA")

name, age, course = student

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

print()

# ----------------------------------------
# Unpacking Numbers
# ----------------------------------------

numbers = (10, 20, 30)

a, b, c = numbers

print("a :", a)
print("b :", b)
print("c :", c)

print()

# ----------------------------------------
# Unpacking with *
# ----------------------------------------

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First  :", first)
print("Middle :", middle)
print("Last   :", last)

print()

# ----------------------------------------
# Ignore Values using _
# ----------------------------------------

data = ("Python", 100, "Programming")

language, _, type_of_data = data

print("Language :", language)
print("Type     :", type_of_data)

print()

# ----------------------------------------
# Swapping Variables using Tuple
# ----------------------------------------

x = 10
y = 20

print("Before Swap:")
print("x =", x)
print("y =", y)

x, y = y, x

print("After Swap:")
print("x =", x)
print("y =", y)

print()

# ----------------------------------------
# Unpacking Nested Tuple
# ----------------------------------------

student = ("Manas", (20, "BCA"))

name, (age, course) = student

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

print()

# ----------------------------------------
# Traversal with Tuple Unpacking
# ----------------------------------------

students = (
    ("Manas", 85),
    ("Rahul", 78),
    ("Aman", 92)
)

for name, marks in students:
    print("Name :", name, "| Marks :", marks)
