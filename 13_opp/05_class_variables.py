# 05_class_variables.py

# Object-Oriented Programming (OOP)
# Topic: Class Variables
#
# A class variable belongs to the class rather than to one
# particular object. It is shared by objects of the class.


# ------------------------------------------------------------
# Example 1: Basic Class Variable
# ------------------------------------------------------------

class Student:
    school = "ABC School"


student1 = Student()
student2 = Student()

print("Student 1 School:", student1.school)
print("Student 2 School:", student2.school)


# ------------------------------------------------------------
# Example 2: Class Variable with Instance Variables
# ------------------------------------------------------------

class Student:
    school = "ABC School"

    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Rahul", "BCA")
student2 = Student("Priya", "BCA")

print("\nStudent 1:")
print("Name:", student1.name)
print("Course:", student1.course)
print("School:", student1.school)

print("\nStudent 2:")
print("Name:", student2.name)
print("Course:", student2.course)
print("School:", student2.school)


# ------------------------------------------------------------
# Example 3: Changing a Class Variable
# ------------------------------------------------------------

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Aman")
student2 = Student("Neha")

print("\nBefore Change:")
print(student1.school)
print(student2.school)

Student.school = "XYZ School"

print("\nAfter Change:")
print(student1.school)
print(student2.school)


# ------------------------------------------------------------
# Example 4: Real-Life Company Example
# ------------------------------------------------------------

class Employee:
    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Rahul", 35000)
employee2 = Employee("Priya", 40000)

print("\nEmployee 1:")
print("Name:", employee1.name)
print("Salary:", employee1.salary)
print("Company:", employee1.company)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("Salary:", employee2.salary)
print("Company:", employee2.company)


# ------------------------------------------------------------
# Example 5: Company Name Change
# ------------------------------------------------------------

Employee.company = "ABC Technologies"

print("\nUpdated Company:")
print(employee1.company)
print(employee2.company)


# ------------------------------------------------------------
# Example 6: Class Variable for Object Counting
# ------------------------------------------------------------

class Product:
    product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1


product1 = Product("Laptop", 55000)
product2 = Product("Mouse", 1500)
product3 = Product("Keyboard", 2500)

print("\nProducts Created:", Product.product_count)


# ------------------------------------------------------------
# Example 7: Class Variable vs Instance Variable
# ------------------------------------------------------------

class StudentInfo:
    school = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = StudentInfo("Rahul", 85)
student2 = StudentInfo("Priya", 92)

print("\nStudent Information:")
print(student1.name, student1.marks, student1.school)
print(student2.name, student2.marks, student2.school)


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. Class variables belong to the class.
# 2. They are shared by objects of the class.
# 3. They are defined inside the class but outside methods.
# 4. They can be accessed using ClassName.variable.
# 5. They can also be accessed using an object.
# 6. Changing the class variable affects objects that use it.
# 7. Instance variables belong to individual objects.
