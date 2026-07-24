"""
=========================================================
Topic       : Return Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Example 1 : Function with Return
# ----------------------------------------

def square(number):
    return number * number

result = square(5)
print("Square :", result)

print()

# ----------------------------------------
# Example 2 : Return Sum of Two Numbers
# ----------------------------------------

def add(a, b):
    return a + b

answer = add(10, 20)
print("Addition :", answer)

print()

# ----------------------------------------
# Example 3 : Return Count of Digits
# ----------------------------------------

def count_digits(number):

    count = 0

    while number > 0:
        count += 1
        number = number // 10

    return count

print("Count of Digits :", count_digits(12345))

print()

# ----------------------------------------
# Example 4 : Return Sum of Digits
# ----------------------------------------

def sum_of_digits(number):

    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    return total

print("Sum of Digits :", sum_of_digits(12345))

print()

# ----------------------------------------
# Example 5 : Return String
# ----------------------------------------

def welcome(name):
    return f"Welcome, {name}!"

print(welcome("Manas"))
