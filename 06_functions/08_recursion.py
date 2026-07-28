"""
=========================================================
Topic       : Recursion
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Example 1 : Print Numbers (1 to 5)
# ----------------------------------------

def print_numbers(n):
    if n > 5:
        return
    print(n)
    print_numbers(n + 1)

print_numbers(1)

print()

# ----------------------------------------
# Example 2 : Factorial Using Recursion
# ----------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 :", factorial(5))

print()

# ----------------------------------------
# Example 3 : Sum of Natural Numbers
# ----------------------------------------

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

print("Sum :", sum_numbers(5))

print()

# ----------------------------------------
# Example 4 : Fibonacci Series
# ----------------------------------------

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = 7

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
