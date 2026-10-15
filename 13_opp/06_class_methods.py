# 06_class_methods.py

# Object-Oriented Programming (OOP)
# Topic: Class Methods
#
# A class method works with the class rather than a particular object.
# It uses the @classmethod decorator.
# Its first parameter is conventionally named cls.


# ------------------------------------------------------------
# Example 1: Basic Class Method
# ------------------------------------------------------------

class Student:
    school = "ABC School"

    @classmethod
    def display_school(cls):
        print("School:", cls.school)


Student.display_school()


# ------------------------------------------------------------
# Example 2: Updating a Class Variable
# ------------------------------------------------------------

class Employee:
    company = "Tech Solutions"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


print("\nCompany Before Change:", Employee.company)
Employee.change_company("ABC Technologies")
print("Company After Change:", Employee.company)


# ------------------------------------------------------------
# Example 3: Calling a Class Method Through an Object
# ------------------------------------------------------------

class Course:
    course_name = "Python Basics"

    @classmethod
    def display_course(cls):
        print("Course:", cls.course_name)


course1 = Course()
course1.display_course()


# ------------------------------------------------------------
# Example 4: Real-Life Product Example
# ------------------------------------------------------------

class Product:
    tax_rate = 18

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Tax Rate:", Product.tax_rate, "%")


product1 = Product("Laptop", 55000)
product2 = Product("Mobile", 25000)

print("\nBefore Tax Rate Change:")
product1.display()
product2.display()

Product.change_tax_rate(20)

print("\nAfter Tax Rate Change:")
product1.display()
product2.display()


# ------------------------------------------------------------
# Example 5: Alternative Constructor Using a Class Method
# ------------------------------------------------------------

class StudentRecord:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_text(cls, text):
        name, marks = text.split(",")
        return cls(name, int(marks))

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = StudentRecord("Rahul", 85)
student2 = StudentRecord.from_text("Priya,92")

print("\nStudent 1:")
student1.display()

print("\nStudent 2:")
student2.display()


# ------------------------------------------------------------
# Example 6: Class Method for Object Counting
# ------------------------------------------------------------

class Account:
    account_count = 0

    def __init__(self, holder):
        self.holder = holder
        Account.account_count += 1

    @classmethod
    def display_count(cls):
        print("Total Accounts:", cls.account_count)


account1 = Account("Rahul")
account2 = Account("Priya")
account3 = Account("Aman")

print("\nAccount Count:")
Account.display_count()


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. Use @classmethod to define a class method.
# 2. The first parameter is conventionally named cls.
# 3. cls refers to the class itself.
# 4. Class methods can read or update class variables.
# 5. They can be called using the class name.
# 6. They can also be called through an object.
# 7. A class method can be used as an alternative constructor.
