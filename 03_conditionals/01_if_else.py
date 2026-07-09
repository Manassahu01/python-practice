"""
=========================================================
Topic       : If and If-Else Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
The 'if' statement executes a block of code only if the
condition is True.

The 'if-else' statement executes one block if the
condition is True, otherwise it executes another block.

Syntax:

if condition:
    statement

if condition:
    statement
else:
    statement
"""

print("=" * 60)
print("IF STATEMENT")
print("=" * 60)

# Example 1

age = 20

if age >= 18:
    print("Eligible for Voting")

print()

# Example 2

marks = 85

if marks >= 33:
    print("Pass")

print()

# Example 3

number = 15

if number > 0:
    print("Positive Number")

print()

# Example 4

salary = 40000

if salary >= 30000:
    print("Eligible for Loan")

print()

# Example 5

temperature = 35

if temperature > 30:
    print("Weather is Hot")

print()

print("=" * 60)
print("IF ELSE STATEMENT")
print("=" * 60)

# Example 1

age = 16

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")

print()

# Example 2

number = 11

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print()

# Example 3

marks = 28

if marks >= 33:
    print("Pass")
else:
    print("Fail")

print()

# Example 4

temperature = 25

if temperature > 30:
    print("Hot Weather")
else:
    print("Normal Weather")

print()

# Example 5

balance = 500

if balance >= 1000:
    print("Withdrawal Allowed")
else:
    print("Insufficient Balance")

print()

# Example 6

password = "python123"

if password == "python123":
    print("Login Successful")
else:
    print("Invalid Password")

print()

# Example 7

num = -10

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")

print()

# Example 8

username = "Manas"

if username == "Manas":
    print("Welcome Manas")
else:
    print("Unknown User")

print()

print("=" * 60)
print("END OF IF & IF ELSE")
print("=" * 60)