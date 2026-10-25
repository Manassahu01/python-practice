# 09_method_overriding.py

# Object-Oriented Programming (OOP)
# Topic: Method Overriding
#
# Method overriding happens when a child class defines a method
# with the same name as a method in its parent class.
# The child class version is used for child objects.


# ------------------------------------------------------------
# Example 1: Basic Method Overriding
# ------------------------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


animal1 = Animal()
dog1 = Dog()

animal1.sound()
dog1.sound()


# ------------------------------------------------------------
# Example 2: Overriding a Parent Method
# ------------------------------------------------------------

class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def introduce(self):
        print("I am a student.")


person1 = Person()
student1 = Student()

print("\nIntroduction:")
person1.introduce()
student1.introduce()


# ------------------------------------------------------------
# Example 3: Using super() with Overriding
# ------------------------------------------------------------

class Employee:
    def display_role(self):
        print("Role: Employee")


class Manager(Employee):
    def display_role(self):
        super().display_role()
        print("Additional Role: Manager")


manager1 = Manager()

print("\nManager Role:")
manager1.display_role()


# ------------------------------------------------------------
# Example 4: Real-Life Payment Methods
# ------------------------------------------------------------

class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)


class CardPayment(Payment):
    def pay(self, amount):
        print("Processing card payment of", amount)


class UpiPayment(Payment):
    def pay(self, amount):
        print("Processing UPI payment of", amount)


card = CardPayment()
upi = UpiPayment()

print("\nPayment Examples:")
card.pay(1500)
upi.pay(750)


# ------------------------------------------------------------
# Example 5: Overriding with Different Calculations
# ------------------------------------------------------------

class Discount:
    def calculate(self, price):
        return 0


class FestivalDiscount(Discount):
    def calculate(self, price):
        return price * 0.10


class PremiumDiscount(Discount):
    def calculate(self, price):
        return price * 0.20


price = 2000

print("\nDiscount Examples:")
print("Regular Discount:", Discount().calculate(price))
print("Festival Discount:", FestivalDiscount().calculate(price))
print("Premium Discount:", PremiumDiscount().calculate(price))


# ------------------------------------------------------------
# Example 6: Real-Life Vehicle Example
# ------------------------------------------------------------

class Vehicle:
    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car engine is starting.")


class ElectricCar(Vehicle):
    def start(self):
        print("Electric car is powering on silently.")


print("\nVehicle Examples:")
Vehicle().start()
Car().start()
ElectricCar().start()


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. A child class can redefine a method from its parent class.
# 2. The child class method is used when called on a child object.
# 3. super() can call the parent class implementation.
# 4. Method overriding allows child classes to provide specialized behavior.
