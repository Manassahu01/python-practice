# 04_instance_methods.py

# Object-Oriented Programming (OOP)
# Topic: Instance Methods
#
# An instance method is a function defined inside a class.
# It works with the data of a particular object.
# The first parameter is usually self.


# ------------------------------------------------------------
# Example 1: Basic Instance Method
# ------------------------------------------------------------

class Student:

    def display(self):
        print("This is a student.")


student1 = Student()
student1.display()


# ------------------------------------------------------------
# Example 2: Instance Method with Instance Variables
# ------------------------------------------------------------

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Rahul", "BCA")

print("\nStudent Information:")
student1.display()


# ------------------------------------------------------------
# Example 3: Calculate Total Marks
# ------------------------------------------------------------

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total_marks(self):
        return self.marks1 + self.marks2 + self.marks3


student1 = Student("Aman", 80, 75, 90)

print("\nStudent:", student1.name)
print("Total Marks:", student1.total_marks())


# ------------------------------------------------------------
# Example 4: Calculate Average
# ------------------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


student1 = Student("Priya", [80, 85, 90, 75, 88])

print("\nStudent:", student1.name)
print("Average Marks:", student1.average())


# ------------------------------------------------------------
# Example 5: Real-Life Bank Account
# ------------------------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


account1 = BankAccount("Rahul", 25000)

print("\nBank Account:")
account1.display_balance()

account1.deposit(5000)

print("After Deposit:")
account1.display_balance()


# ------------------------------------------------------------
# Example 6: Real-Life Employee
# ------------------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Neha", 35000)

print("\nEmployee Information:")
employee1.display()

employee1.increase_salary(5000)

print("After Salary Increase:")
employee1.display()


# ------------------------------------------------------------
# Example 7: Student Pass or Fail
# ------------------------------------------------------------

class StudentResult:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"


student1 = StudentResult("Aman", 72)
student2 = StudentResult("Riya", 28)

print("\nStudent Result:")
print(student1.name, ":", student1.result())
print(student2.name, ":", student2.result())


# ------------------------------------------------------------
# Example 8: Multiple Objects Using the Same Method
# ------------------------------------------------------------

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")


car1 = Car("Toyota", 180)
car2 = Car("Honda", 160)

print("\nCar 1:")
car1.display()

print("\nCar 2:")
car2.display()


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. Instance methods are defined inside a class.
# 2. They usually take self as the first parameter.
# 3. self refers to the current object.
# 4. Instance methods can access instance variables.
# 5. Instance methods can modify object data.
# 6. Instance methods can return values.
# 7. Different objects can use the same method with different data.
