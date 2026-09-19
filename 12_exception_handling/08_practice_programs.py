# 08_practice_programs.py

# Practice programs for Exception Handling.

# 1. Divide Two Numbers
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print("Result:", result)
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 2. Age Validation
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Valid age:", age)
except ValueError as error:
    print("Age Error:", error)

# 3. Marks Validation
try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    print("Valid marks:", marks)
except ValueError as error:
    print("Marks Error:", error)

# 4. List Index
subjects = ["Python", "SQL", "Power BI", "Excel"]
try:
    number = int(input("Enter subject number (1-4): "))
    print("Subject:", subjects[number - 1])
except ValueError:
    print("Please enter a number.")
except IndexError:
    print("Please enter a number between 1 and 4.")

# 5. Convert Number
try:
    value = input("Enter a number: ")
    number = float(value)
    print("Number:", number)
except ValueError:
    print("Invalid number.")

# 6. Read a File
file_name = "student_notes.txt"
try:
    with open(file_name, "r") as file:
        file_content = file.read()
    print("File Content:")
    print(file_content)
except FileNotFoundError:
    print("File does not exist.")

# 7. Student Result
try:
    marks = int(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 35:
        print("Result: Pass")
    else:
        print("Result: Fail")
except ValueError as error:
    print("Result Error:", error)

# 8. Shopping Quantity
try:
    quantity = int(input("Enter product quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    print("Quantity:", quantity)
except ValueError as error:
    print("Quantity Error:", error)

# 9. Calculate Average
try:
    marks = [70, 80, 65, 90, 85]
    total = sum(marks)
    average = total / len(marks)
    print("Total:", total)
    print("Average:", average)
except ZeroDivisionError:
    print("Cannot calculate average.")
except TypeError:
    print("Invalid marks data.")

# 10. Simple Login
correct_password = "python123"
try:
    password = input("Enter password: ")
    if password != correct_password:
        raise ValueError("Incorrect password.")
    print("Login successful.")
except ValueError as error:
    print("Login Error:", error)

# 11. Custom Exception
class InvalidSalaryError(Exception):
    pass

try:
    salary = float(input("Enter monthly salary: "))
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")
    print("Valid salary:", salary)
except ValueError:
    print("Please enter a valid salary.")
except InvalidSalaryError as error:
    print("Salary Error:", error)

# 12. Safe Dictionary Access
student = {"name": "Rahul", "course": "Python", "marks": 85}
try:
    key = input("Enter student detail (name/course/marks): ")
    print("Value:", student[key])
except KeyError:
    print("This student detail does not exist.")

# 13. Multiple Exceptions
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print("Result:", result)
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)

# 14. Finally Example
try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid input.")
finally:
    print("Program execution completed.")

# 15. Raise an Exception
try:
    study_hours = int(input("Enter today's study hours: "))
    if study_hours < 0 or study_hours > 12:
        raise ValueError("Study hours must be between 0 and 12.")
    print("Study hours:", study_hours)
except ValueError as error:
    print("Study Hours Error:", error)

# Key Points
# 1. Practice handling common built-in exceptions.
# 2. Use raise when you want to validate a value yourself.
# 3. Use custom exceptions for meaningful application errors.
# 4. Use finally for code that should execute at the end.
# 5. Keep exception handling simple and readable.
