# 07_exception_programs.py

# Simple real-life programs for practicing exception handling.


# ------------------------------------------------------------
# Program 1: Safe Division
# ------------------------------------------------------------

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

    print("Division result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Second number cannot be zero.")


# ------------------------------------------------------------
# Program 2: Student Marks Validation
# ------------------------------------------------------------

try:
    marks = int(input("Enter student marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)

except ValueError as error:
    print("Marks Error:", error)


# ------------------------------------------------------------
# Program 3: Access Student Record
# ------------------------------------------------------------

students = ["Rahul", "Aman", "Priya", "Neha"]

try:
    number = int(input("Enter student number (1-4): "))

    print("Student:", students[number - 1])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("Student number must be between 1 and 4.")


# ------------------------------------------------------------
# Program 4: Salary Validation
# ------------------------------------------------------------

try:
    salary = float(input("Enter monthly salary: "))

    if salary < 0:
        raise ValueError("Salary cannot be negative.")

    print("Monthly salary:", salary)

except ValueError as error:
    print("Salary Error:", error)


# ------------------------------------------------------------
# Program 5: Calculate Average Marks
# ------------------------------------------------------------

try:
    marks = [75, 82, 68, 91, 84]

    total = sum(marks)
    average = total / len(marks)

    print("Total marks:", total)
    print("Average marks:", average)

except ZeroDivisionError:
    print("Cannot calculate average.")

except TypeError:
    print("Marks must contain numbers.")


# ------------------------------------------------------------
# Program 6: File Handling
# ------------------------------------------------------------

file_name = "student_records.txt"

try:
    with open(file_name, "r") as file:
        data = file.read()

    print("Student Records:")
    print(data)

except FileNotFoundError:
    print("File not found:", file_name)

except PermissionError:
    print("You do not have permission to read this file.")


# ------------------------------------------------------------
# Program 7: Login Validation
# ------------------------------------------------------------

correct_password = "python123"

try:
    password = input("Enter password: ")

    if password != correct_password:
        raise ValueError("Incorrect password.")

    print("Login successful.")

except ValueError as error:
    print("Login Error:", error)


# ------------------------------------------------------------
# Program 8: Shopping Quantity
# ------------------------------------------------------------

try:
    quantity = int(input("Enter product quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    print("Product quantity:", quantity)

except ValueError as error:
    print("Quantity Error:", error)


# ------------------------------------------------------------
# Program 9: Student Result
# ------------------------------------------------------------

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 35:
        print("Result: Pass")
    else:
        print("Result: Fail")

except ValueError as error:
    print("Result Error:", error)


# ------------------------------------------------------------
# Program 10: Safe List Access
# ------------------------------------------------------------

subjects = ["Python", "SQL", "Power BI", "Excel"]

try:
    number = int(input("Enter subject number (1-4): "))

    print("Selected subject:", subjects[number - 1])

except ValueError:
    print("Please enter a number.")

except IndexError:
    print("Please choose a number between 1 and 4.")


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------
# 1. Use try for code that may cause an exception.
# 2. Use except to handle the exception.
# 3. Different exceptions can have different except blocks.
# 4. ValueError handles invalid input values.
# 5. ZeroDivisionError occurs when dividing by zero.
# 6. IndexError occurs when a list index does not exist.
# 7. FileNotFoundError occurs when a file cannot be found.
# 8. raise can be used to create an error ourselves.
