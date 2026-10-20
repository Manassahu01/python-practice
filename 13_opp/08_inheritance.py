# 08_inheritance.py

# Object-Oriented Programming (OOP)
# Topic: Inheritance
# Inheritance allows a child class to reuse attributes and methods
# from a parent class.


# ------------------------------------------------------------
# Example 1: Basic Inheritance
# ------------------------------------------------------------

class Animal:
    def eat(self):
        print("This animal eats food.")


class Dog(Animal):
    pass


dog1 = Dog()
dog1.eat()


# ------------------------------------------------------------
# Example 2: Parent and Child Classes
# ------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print("Course:", self.course)


student1 = Student("Rahul", 21, "BCA")

print("\nStudent Information:")
student1.display_student()


# ------------------------------------------------------------
# Example 3: Real-Life Employee Inheritance
# ------------------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)


manager1 = Manager("Priya", 65000, "IT")

print("\nManager Information:")
manager1.display_manager()


# ------------------------------------------------------------
# Example 4: Inheriting Methods
# ------------------------------------------------------------

class Vehicle:
    def start(self):
        print("Vehicle has started.")

    def stop(self):
        print("Vehicle has stopped.")


class Car(Vehicle):
    def drive(self):
        print("Car is moving.")


car1 = Car()

print("\nCar Actions:")
car1.start()
car1.drive()
car1.stop()


# ------------------------------------------------------------
# Example 5: Child-Specific Method
# ------------------------------------------------------------

class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(self.username, "logged in.")


class Admin(User):
    def delete_user(self, username):
        print("Admin", self.username, "deleted user", username)


admin1 = Admin("manas_admin")

print("\nAdmin Actions:")
admin1.login()
admin1.delete_user("test_user")


# ------------------------------------------------------------
# Example 6: Checking Inheritance
# ------------------------------------------------------------

class Device:
    pass


class Laptop(Device):
    pass


laptop1 = Laptop()

print("\nIs Laptop a subclass of Device?", issubclass(Laptop, Device))
print("Is laptop1 an instance of Laptop?", isinstance(laptop1, Laptop))
print("Is laptop1 an instance of Device?", isinstance(laptop1, Device))


# ------------------------------------------------------------
# Example 7: Multilevel Inheritance
# ------------------------------------------------------------

class LivingThing:
    def breathe(self):
        print("Living things breathe.")


class Animal(LivingThing):
    def move(self):
        print("Animals can move.")


class Bird(Animal):
    def fly(self):
        print("Many birds can fly.")


bird1 = Bird()

print("\nBird Actions:")
bird1.breathe()
bird1.move()
bird1.fly()


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. Inheritance lets a child class reuse parent class functionality.
# 2. The parent class is also called a base class.
# 3. The child class is also called a derived class.
# 4. Use class Child(Parent) to define inheritance.
# 5. super() can call methods from the parent class.
# 6. A child class can add its own attributes and methods.
# 7. Python supports single, multiple, multilevel, and hierarchical
#    inheritance patterns.
