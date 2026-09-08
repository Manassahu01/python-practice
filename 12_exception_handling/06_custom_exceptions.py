# 06_custom_exceptions.py

class InvalidMarksError(Exception):
    pass


# Example 1: Custom exception for marks

marks = 105

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)

except InvalidMarksError as error:
    print("Invalid marks:", error)


# Example 2: Custom exception for age

class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    print("Valid age:", age)

except ValueError:
    print("Please enter a valid number.")

except InvalidAgeError as error:
    print("Invalid age:", error)


# Example 3: Student result

class FailedStudentError(Exception):
    pass


student_name = "Rahul"
student_marks = 32
passing_marks = 35

try:
    if student_marks < passing_marks:
        raise FailedStudentError(
            f"{student_name} has failed because marks are below {passing_marks}."
        )

    print(student_name, "has passed.")

except FailedStudentError as error:
    print("Result:", error)


# Example 4: Study hours

class InvalidStudyHoursError(Exception):
    pass


study_hours = 15

try:
    if study_hours < 0 or study_hours > 12:
        raise InvalidStudyHoursError(
            "Study hours must be between 0 and 12 per day."
        )

    print("Study hours:", study_hours)

except InvalidStudyHoursError as error:
    print("Invalid study hours:", error)


# Example 5: Custom exception inside a function

class InvalidSalaryError(Exception):
    pass


def check_salary(salary):
    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

    print("Valid salary:", salary)


try:
    check_salary(25000)

except InvalidSalaryError as error:
    print("Salary Error:", error)


# Key Points:
# 1. Custom exceptions are created by inheriting from Exception.
# 2. Use raise to generate a custom exception.
# 3. Custom exceptions make errors easier to understand.
# 4. Handle custom exceptions using except.
