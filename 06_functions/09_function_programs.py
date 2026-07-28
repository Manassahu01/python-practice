"""
=========================================================
Topic       : Function Practice Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Check Even or Odd
# ----------------------------------------

def even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

even_odd(12)

print()

# ----------------------------------------
# Program 2 : Find Maximum
# ----------------------------------------

def maximum(a, b):
    if a > b:
        return a
    return b

print("Maximum :", maximum(15, 25))

print()

# ----------------------------------------
# Program 3 : Check Prime Number
# ----------------------------------------

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

num = 13

if is_prime(num):
    print(num, "is Prime")
else:
    print(num, "is Not Prime")

print()

# ----------------------------------------
# Program 4 : Factorial
# ----------------------------------------

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

print("Factorial :", factorial(5))

print()

# ----------------------------------------
# Program 5 : Sum of Digits
# ----------------------------------------

def sum_of_digits(number):

    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total

print("Sum of Digits :", sum_of_digits(12345))
