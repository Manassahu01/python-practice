# 07_static_methods.py

# Object-Oriented Programming (OOP)
# Topic: Static Methods
#
# A static method does not automatically receive self or cls.
# It is defined using the @staticmethod decorator.
# It is useful for utility tasks related to a class.


# ------------------------------------------------------------
# Example 1: Basic Static Method
# ------------------------------------------------------------

class Calculator:

    @staticmethod
    def add(number1, number2):
        return number1 + number2


print("Sum:", Calculator.add(10, 5))


# ------------------------------------------------------------
# Example 2: Calculator Operations
# ------------------------------------------------------------

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero."
        return a / b


print("\nAddition:", Calculator.add(12, 4))
print("Subtraction:", Calculator.subtract(12, 4))
print("Multiplication:", Calculator.multiply(12, 4))
print("Division:", Calculator.divide(12, 4))
print("Division by zero:", Calculator.divide(12, 0))


# ------------------------------------------------------------
# Example 3: Check Even or Odd
# ------------------------------------------------------------

class NumberChecker:

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print("\nIs 10 even?", NumberChecker.is_even(10))
print("Is 7 even?", NumberChecker.is_even(7))


# ------------------------------------------------------------
# Example 4: Product Price Validation
# ------------------------------------------------------------

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def is_valid_price(price):
        return price >= 0


print("\nValid price 1500?", Product.is_valid_price(1500))
print("Valid price -100?", Product.is_valid_price(-100))


# ------------------------------------------------------------
# Example 5: Basic Email Format Check
# ------------------------------------------------------------

class EmailValidator:

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email


print("\nEmail check:")
print("user@example.com:", EmailValidator.is_valid_email("user@example.com"))
print("invalid-email:", EmailValidator.is_valid_email("invalid-email"))


# ------------------------------------------------------------
# Example 6: Temperature Conversion
# ------------------------------------------------------------

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


print("\n25 Celsius in Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(25))
print("77 Fahrenheit in Celsius:", TemperatureConverter.fahrenheit_to_celsius(77))


# ------------------------------------------------------------
# Example 7: Static Method Called Through an Object
# ------------------------------------------------------------

class Greeting:

    @staticmethod
    def say_hello(name):
        print("Hello,", name)


greeting = Greeting()
greeting.say_hello("Rahul")


# ------------------------------------------------------------
# Example 8: Compare Method Types
# ------------------------------------------------------------

class Demo:

    category = "Python OOP"

    def instance_method(self):
        return "Uses self: works with object data"

    @classmethod
    def class_method(cls):
        return "Uses cls: works with class data"

    @staticmethod
    def static_method():
        return "Uses neither self nor cls automatically"


demo = Demo()

print("\nMethod Comparison:")
print(demo.instance_method())
print(Demo.class_method())
print(Demo.static_method())


# ------------------------------------------------------------
# Key Points
# ------------------------------------------------------------

# 1. Use @staticmethod to define a static method.
# 2. It does not automatically receive self or cls.
# 3. It can be called using the class name or an object.
# 4. Static methods are useful for related utility functions.
# 5. Use instance methods when you need object data.
# 6. Use class methods when you need class-level data.
