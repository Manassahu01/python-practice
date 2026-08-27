"""
=========================================================
Topic       : else and finally
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Real-Life Example:
# A student enters marks and the program calculates
# an average. The else block runs when no exception
# occurs, while finally runs whether an exception occurs.

# ----------------------------------------
# Example 1 : try + except + else
# ----------------------------------------

print("Example 1: Calculate Average")

try:
    total_marks = int(input("Enter total marks: "))
    subjects = int(input("Enter number of subjects: "))

    average = total_marks / subjects

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Number of subjects cannot be zero.")

else:
    print("Average Marks:", average)
    print("Calculation completed successfully.")

print()

# ----------------------------------------
# Example 2 : try + except + finally
# ----------------------------------------

print("Example 2: Student Age")

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Invalid age. Please enter a number.")

finally:
    print("Age input process completed.")

print()

# ----------------------------------------
# Example 3 : try + except + else + finally
# ----------------------------------------

print("Example 3: Student Result")

try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as error:
    print("Error:", error)

else:
    print("Valid Marks:", marks)

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

finally:
    print("Result processing completed.")

print()

# ----------------------------------------
# Example 4 : File Handling with finally
# ----------------------------------------

file = None

try:
    file = open("student_result.txt", "w")
    file.write("Student: Manas Sahu\n")
    file.write("Result: Pass\n")

except OSError:
    print("Unable to access the file.")

else:
    print("Student result saved successfully.")

finally:
    if file is not None:
        file.close()

    print("File operation completed.")

print()

# ----------------------------------------
# Important Concept
# ----------------------------------------
# else    -> runs only when no exception occurs
# finally -> runs whether an exception occurs or not
