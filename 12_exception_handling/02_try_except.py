"""
=========================================================
Topic       : try and except
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Real-Life Example:
# A student enters information into a program.
# try-except prevents the program from crashing
# when invalid data is entered.

# ----------------------------------------
# Example 1 : Handling Invalid Number
# ----------------------------------------

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Invalid input! Please enter a number.")

print()

# ----------------------------------------
# Example 2 : Handling Division by Zero
# ----------------------------------------

try:
    total_marks = 500
    subjects = int(input("Enter number of subjects: "))

    average = total_marks / subjects

    print("Average Marks:", average)

except ZeroDivisionError:
    print("Number of subjects cannot be zero.")

print()

# ----------------------------------------
# Example 3 : Handling List Index Error
# ----------------------------------------

subjects = ["Python", "SQL", "NumPy"]

try:
    index = int(input("Enter subject index (0-2): "))
    print("Selected Subject:", subjects[index])

except IndexError:
    print("Invalid index! Choose an index from 0 to 2.")

except ValueError:
    print("Please enter a valid number.")

print()

# ----------------------------------------
# Example 4 : General Exception Handling
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except Exception as error:
    print("Something went wrong.")
    print("Error:", error)

print()

# ----------------------------------------
# Example 5 : Program Continues After Error
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    print("Double:", number * 2)

except ValueError:
    print("Invalid number entered.")

print("Program continues normally after exception handling.")
