"""
=========================================================
Topic       : If-Elif-Else Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
The if-elif-else statement is used when there are
multiple conditions.

Syntax:

if condition:
    statement

elif condition:
    statement

elif condition:
    statement

else:
    statement
"""

print("=" * 60)
print("IF ELIF ELSE STATEMENT")
print("=" * 60)

# ----------------------------------------
# Example 1 : Student Grade
# ----------------------------------------

marks = 78

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

elif marks >= 33:
    print("Grade C")

else:
    print("Fail")

print()

# ----------------------------------------
# Example 2 : Largest Number
# ----------------------------------------

a = 15
b = 40

if a > b:
    print("a is Greater")

elif b > a:
    print("b is Greater")

else:
    print("Both are Equal")

print()

# ----------------------------------------
# Example 3 : Positive, Negative or Zero
# ----------------------------------------

num = -10

if num > 0:
    print("Positive Number")

elif num < 0:
    print("Negative Number")

else:
    print("Zero")

print()

# ----------------------------------------
# Example 4 : Age Category
# ----------------------------------------

age = 22

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")

print()

# ----------------------------------------
# Example 5 : Day Number
# ----------------------------------------

day = 5

if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

else:
    print("Invalid Day")

print()

# ----------------------------------------
# Example 6 : Calculator
# ----------------------------------------

a = 15
b = 5
choice = "+"

if choice == "+":
    print(a + b)

elif choice == "-":
    print(a - b)

elif choice == "*":
    print(a * b)

elif choice == "/":
    print(a / b)

else:
    print("Invalid Operator")

print()

# ----------------------------------------
# Example 7 : Even or Odd
# ----------------------------------------

number = 21

if number % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

print()

# ----------------------------------------
# Example 8 : Login System
# ----------------------------------------

username = "admin"

if username == "admin":
    print("Welcome Admin")

elif username == "student":
    print("Welcome Student")

else:
    print("Unknown User")

print()

print("=" * 60)
print("END OF IF ELIF ELSE")
print("=" * 60)