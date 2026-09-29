# 01_class_and_object.py

# Object-Oriented Programming (OOP)
# Topic: Class and Object


# ------------------------------------------------------------
# Example 1: Creating a Simple Class
# ------------------------------------------------------------

class Student:
    pass


student1 = Student()

print("Student object:", student1)


# ------------------------------------------------------------
# Example 2: Class with Attributes
# ------------------------------------------------------------

class Student:
    name = "Rahul"
    course = "BCA"
    age = 21


student1 = Student()

print("Name:", student1.name)
print("Course:", student1.course)
print("Age:", student1.age)


# ------------------------------------------------------------
# Example 3: Creating Multiple Objects
# ------------------------------------------------------------

class Student:
    name = "Unknown"
    course = "Unknown"


student1 = Student()
student2 = Student()

student1.name = "Rahul"
student1.course = "BCA"

student2.name = "Priya"
student2.course = "BCA"

print("\nStudent 1:")
print("Name:", student1.name)
print("Course:", student1.course)

print("\nStudent 2:")
print("Name:", student2.name)
print("Course:", student2.course)


# ------------------------------------------------------------
# Example 4: Real-Life Bank Account Example
# ------------------------------------------------------------

class BankAccount:
    account_type = "Savings"
    bank_name = "ABC Bank"


account1 = BankAccount()
account2 = BankAccount()

account1.account_holder = "Rahul"
account1.balance = 25000

account2.account_holder = "Priya"
account2.balance = 40000

print("\nBank Account 1:")
print("Bank:", account1.bank_name)
print("Account Holder:", account1.account_holder)
print("Account Type:", account1.account_type)
print("Balance:", account1.balance)

print("\nBank Account 2:")
print("Bank:", account2.bank_name)
print("Account Holder:", account2.account_holder)
print("Account Type:", account2.account_type)
print("Balance:", account2.balance)


# ------------------------------------------------------------
# Example 5: Employee Objects
# ------------------------------------------------------------

class Employee:
    company = "Tech Solutions"


employee1 = Employee()
employee2 = Employee()

employee1.name = "Aman"
employee1.salary = 30000

employee2.name = "Neha"
employee2.salary = 35000

print("\nEmployee 1:")
print("Name:", employee1.name)
print("Company:", employee1.company)
print("Salary:", employee1.salary)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("Company:", employee2.company)
print("Salary:", employee2.salary)


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. A class is a blueprint for objects.
# 2. An object is an instance of a class.
# 3. A class is created using the class keyword.
# 4. An object is created by calling the class.
# 5. Objects can have their own attributes.
# 6. Multiple objects can be created from the same class.
# 7. Classes help organize real-world entities in a program.
