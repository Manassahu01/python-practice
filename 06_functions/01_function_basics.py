"""
=========================================================
Topic       : Function Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Function Without Parameter
# ----------------------------------------

def greeting():
    print("Welcome to Python Functions")


greeting()

print()

# ----------------------------------------
# Function With Parameter
# ----------------------------------------

def display(name):
    print("Hello", name)


display("Manas")

print()

# ----------------------------------------
# Count Number of Digits
# ----------------------------------------

def count_digits(n):

    count = 0

    while n > 0:
        count += 1
        n = n // 10

    return f"Count of Digits : {count}"


print(count_digits(12345))

print()

# ----------------------------------------
# Sum of Digits
# ----------------------------------------

def sum_of_digits(n):

    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return f"Sum of Digits : {total}"


print(sum_of_digits(12345))
