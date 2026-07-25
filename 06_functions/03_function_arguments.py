"""
=========================================================
Topic       : Function Arguments
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Function with One Argument
# ----------------------------------------

def greet(name):
    print("Hello", name)

greet("Manas")

print()

# ----------------------------------------
# Function with Two Arguments
# ----------------------------------------

def add(a, b):
    print("Addition :", a + b)

add(10, 20)

print()

# ----------------------------------------
# Function with Three Arguments
# ----------------------------------------

def student(name, age, course):
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

student("Manas", 20, "BCA")

print()

# ----------------------------------------
# User Input as Arguments
# ----------------------------------------

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

def multiply(a, b):
    print("Multiplication :", a * b)

multiply(num1, num2)

print()

# ----------------------------------------
# Count Digits Using Function Argument
# ----------------------------------------

def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

print("Count of Digits :", count_digits(987654))
