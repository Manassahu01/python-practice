# 02_constructor.py

# Object-Oriented Programming (OOP)
# Topic: Constructor
#
# A constructor is a special method that is automatically called
# when an object is created.
#
# In Python, the constructor is usually written as __init__().
# It is mainly used to initialize object data.


# ------------------------------------------------------------
# Example 1: Basic Constructor
# ------------------------------------------------------------

class Student:

    def __init__(self):
        print("Student object created")


student1 = Student()
student2 = Student()


# ------------------------------------------------------------
# Example 2: Constructor with Parameters
# ------------------------------------------------------------

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Rahul", "BCA")
student2 = Student("Priya", "BCA")

print("\nStudent 1:")
print("Name:", student1.name)
print("Course:", student1.course)

print("\nStudent 2:")
print("Name:", student2.name)
print("Course:", student2.course)


# ------------------------------------------------------------
# Example 3: Student Information
# ------------------------------------------------------------

class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


student1 = Student("Aman", 21, 85)

print("\nStudent Information:")
student1.display()


# ------------------------------------------------------------
# Example 4: Real-Life Bank Account
# ------------------------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account1 = BankAccount("Rahul", 25000)
account2 = BankAccount("Neha", 40000)

print("\nBank Account 1:")
account1.display()

print("\nBank Account 2:")
account2.display()


# ------------------------------------------------------------
# Example 5: Employee Information
# ------------------------------------------------------------

class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


employee1 = Employee("Aman", "IT", 35000)
employee2 = Employee("Neha", "HR", 32000)

print("\nEmployee 1:")
print("Name:", employee1.name)
print("Department:", employee1.department)
print("Salary:", employee1.salary)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("Department:", employee2.department)
print("Salary:", employee2.salary)


# ------------------------------------------------------------
# Example 6: Constructor with Default Values
# ------------------------------------------------------------

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price


product1 = Product("Laptop", 55000)
product2 = Product("Mouse")

print("\nProduct 1:")
print("Name:", product1.name)
print("Price:", product1.price)

print("\nProduct 2:")
print("Name:", product2.name)
print("Price:", product2.price)


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. __init__() is commonly used as a constructor in Python.
# 2. The constructor runs automatically when an object is created.
# 3. It is used to initialize object data.
# 4. self refers to the current object.
# 5. Constructors can accept parameters.
# 6. Constructors can also use default parameter values.
