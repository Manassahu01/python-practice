"""
=========================================================
Topic       : Keyword Arguments
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Keyword Arguments
# ----------------------------------------

def student(name, age, course):
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

student(name="Manas", age=20, course="BCA")

print()

# ----------------------------------------
# Changing Order of Arguments
# ----------------------------------------

student(course="Python", name="Rahul", age=21)

print()

# ----------------------------------------
# Employee Details
# ----------------------------------------

def employee(emp_id, emp_name, department):
    print("Employee ID :", emp_id)
    print("Name        :", emp_name)
    print("Department  :", department)

employee(department="Data Science", emp_name="Manas", emp_id=101)

print()

# ----------------------------------------
# Function with Return
# ----------------------------------------

def add(a, b):
    return a + b

result = add(b=30, a=20)
print("Addition :", result)
