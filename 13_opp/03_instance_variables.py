# 03_instance_variables.py

# Object-Oriented Programming (OOP)
# Topic: Instance Variables
#
# Instance variables belong to a particular object.
# Each object can have its own different values.
# They are usually created using self inside __init__().


# ------------------------------------------------------------
# Example 1: Basic Instance Variables
# ------------------------------------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Rahul", 21)
student2 = Student("Priya", 20)

print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)


# ------------------------------------------------------------
# Example 2: Different Values for Different Objects
# ------------------------------------------------------------

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


employee1 = Employee("Aman", "IT", 35000)
employee2 = Employee("Neha", "HR", 32000)

print("\nEmployee 1:")
print(employee1.name, employee1.department, employee1.salary)

print("\nEmployee 2:")
print(employee2.name, employee2.department, employee2.salary)


# ------------------------------------------------------------
# Example 3: Real-Life Bank Account
# ------------------------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


account1 = BankAccount("Rahul", 25000)
account2 = BankAccount("Priya", 40000)

print("\nBank Account 1:")
print("Holder:", account1.account_holder)
print("Balance:", account1.balance)

print("\nBank Account 2:")
print("Holder:", account2.account_holder)
print("Balance:", account2.balance)


# ------------------------------------------------------------
# Example 4: Updating Instance Variables
# ------------------------------------------------------------

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 55000)

print("\nBefore Update:")
print("Name:", product.name)
print("Price:", product.price)

product.price = 60000

print("\nAfter Update:")
print("Name:", product.name)
print("Price:", product.price)


# ------------------------------------------------------------
# Example 5: Adding an Instance Variable Later
# ------------------------------------------------------------

class Car:

    def __init__(self, brand):
        self.brand = brand


car1 = Car("Toyota")

car1.color = "White"
car1.price = 1200000

print("\nCar Information:")
print("Brand:", car1.brand)
print("Color:", car1.color)
print("Price:", car1.price)


# ------------------------------------------------------------
# Example 6: Instance Variables with Methods
# ------------------------------------------------------------

class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


mobile1 = Mobile("Samsung", 30000)

print("\nMobile Information:")
mobile1.display()


# ------------------------------------------------------------
# Example 7: Instance Variable vs Class Variable
# ------------------------------------------------------------

class StudentInfo:

    school = "ABC School"  # Class variable

    def __init__(self, name, marks):
        self.name = name      # Instance variable
        self.marks = marks    # Instance variable


student1 = StudentInfo("Rahul", 85)
student2 = StudentInfo("Priya", 92)

print("\nStudent Information:")
print(student1.name, student1.marks, student1.school)
print(student2.name, student2.marks, student2.school)


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. Instance variables belong to individual objects.
# 2. They are commonly created using self.
# 3. Different objects can have different values.
# 4. Instance variables are usually initialized in __init__().
# 5. They can be updated after object creation.
# 6. They can be accessed using object.attribute.
# 7. Instance variables are different from class variables.
