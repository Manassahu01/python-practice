"""
=========================================================
Topic       : Default Arguments
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Default Argument
# ----------------------------------------

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Manas")

print()

# ----------------------------------------
# Default Age
# ----------------------------------------

def student(name, age=18):
    print("Name :", name)
    print("Age  :", age)

student("Rahul")
print()

student("Manas", 20)

print()

# ----------------------------------------
# Default Course
# ----------------------------------------

def course_details(name, course="Python"):
    print("Name   :", name)
    print("Course :", course)

course_details("Aman")
print()

course_details("Manas", "Data Science")

print()

# ----------------------------------------
# Calculate Simple Interest
# ----------------------------------------

def simple_interest(p, r=10, t=2):
    si = (p * r * t) / 100
    print("Simple Interest :", si)

simple_interest(10000)
simple_interest(10000, 12, 3)
