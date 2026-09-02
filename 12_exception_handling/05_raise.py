"""
=========================================================
Topic       : raise Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Real-Life Example:
# A student result system should accept marks only between
# 0 and 100. The raise statement creates an exception when
# invalid marks are entered.

# ----------------------------------------
# Example 1 : Raise ValueError
# ----------------------------------------

try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Valid Marks:", marks)

except ValueError as error:
    print("Error:", error)

print()

# ----------------------------------------
# Example 2 : Raise ValueError for Age
# ----------------------------------------

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid Age:", age)

except ValueError as error:
    print("Error:", error)

print()

# ----------------------------------------
# Example 3 : Raise Exception for Empty Name
# ----------------------------------------

try:
    name = input("Enter your name: ")

    if name.strip() == "":
        raise ValueError("Name cannot be empty.")

    print("Student Name:", name)

except ValueError as error:
    print("Error:", error)

print()

# ----------------------------------------
# Example 4 : Raise Exception for Failed Result
# ----------------------------------------

try:
    marks = int(input("Enter marks to check result: "))

    if marks < 40:
        raise Exception("Student has failed the examination.")

    print("Student has passed the examination.")

except Exception as error:
    print("Result Error:", error)

print()

# ----------------------------------------
# Example 5 : Validate Study Hours
# ----------------------------------------

try:
    hours = float(input("Enter daily study hours: "))

    if hours < 0:
        raise ValueError("Study hours cannot be negative.")

    if hours > 24:
        raise ValueError("Study hours cannot exceed 24.")

    print("Valid Study Hours:", hours)

except ValueError as error:
    print("Error:", error)

# ----------------------------------------
# Important Concept
# ----------------------------------------
# raise is used when we want to manually create
# an exception based on our own condition.
