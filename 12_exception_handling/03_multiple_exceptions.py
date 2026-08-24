"""
=========================================================
Topic       : Multiple Exceptions
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Real-Life Example:
# A student enters marks and subject information.
# Different errors can occur depending on the input.

# ----------------------------------------
# Example 1 : Multiple except Blocks
# ----------------------------------------

try:
    total_marks = int(input("Enter total marks: "))
    subjects = int(input("Enter number of subjects: "))

    average = total_marks / subjects

    print("Average Marks:", average)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Number of subjects cannot be zero.")

print()

# ----------------------------------------
# Example 2 : List with Multiple Exceptions
# ----------------------------------------

subjects = ["Python", "SQL", "NumPy"]

try:
    index = int(input("Enter subject index: "))
    subject = subjects[index]

    print("Selected Subject:", subject)

except ValueError:
    print("Index must be a number.")

except IndexError:
    print("Invalid index. Please choose 0, 1, or 2.")

print()

# ----------------------------------------
# Example 3 : Different Operations
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

except TypeError:
    print("Invalid data type.")

print()

# ----------------------------------------
# Example 4 : Multiple Exceptions in One
#             except Block
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Please enter a valid non-zero number.")

print()

# ----------------------------------------
# Example 5 : Catching the Error Object
# ----------------------------------------

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except (ValueError, ZeroDivisionError) as error:
    print("An error occurred.")
    print("Error Type:", type(error).__name__)
    print("Error Message:", error)

print()

print("Program completed successfully.")
