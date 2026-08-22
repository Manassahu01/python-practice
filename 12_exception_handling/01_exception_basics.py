"""
=========================================================
Topic       : Exception Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Real-Life Example:
A student enters marks into a program. If the user enters
invalid data, Python can raise an exception instead of
continuing with incorrect information.
"""

# ----------------------------------------
# Example 1 : ValueError
# ----------------------------------------

print("Example 1: Student Marks")

try:
    marks = int(input("Enter your marks: "))
    print("Your marks are:", marks)

except ValueError:
    print("Invalid input! Please enter marks as a number.")

print()

# ----------------------------------------
# Example 2 : ZeroDivisionError
# ----------------------------------------

print("Example 2: Calculate Average")

try:
    total_marks = 500
    number_of_subjects = int(input("Enter number of subjects: "))

    average = total_marks / number_of_subjects

    print("Average Marks:", average)

except ZeroDivisionError:
    print("Number of subjects cannot be zero.")

print()

# ----------------------------------------
# Example 3 : IndexError
# ----------------------------------------

print("Example 3: Student Subjects")

subjects = ["Python", "SQL", "NumPy"]

try:
    index = int(input("Enter subject index (0-2): "))
    print("Subject:", subjects[index])

except IndexError:
    print("Invalid index! Please choose an index from 0 to 2.")

except ValueError:
    print("Please enter a valid number.")

print()

# ----------------------------------------
# Example 4 : NameError
# ----------------------------------------

print("Example 4: Undefined Variable")

try:
    print(student_name)

except NameError:
    print("The variable 'student_name' is not defined.")

print()

# ----------------------------------------
# Example 5 : TypeError
# ----------------------------------------

print("Example 5: Data Type Error")

try:
    age = 20
    message = "Student age is " + age

    print(message)

except TypeError:
    print("Cannot combine a string and an integer directly.")

print()

# ----------------------------------------
# Important Concept
# ----------------------------------------

print("Exception handling helps programs handle errors safely.")
