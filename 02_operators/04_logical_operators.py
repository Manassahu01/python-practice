"""
=========================================================
Topic       : Logical Operators in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
Logical operators are used to combine two or more
conditions.

Operators:

and
or
not

Output of logical operators is always True or False.
"""

print("=" * 60)
print("LOGICAL OPERATORS")
print("=" * 60)

a = 20
b = 10

print("a =", a)
print("b =", b)

print()

# ----------------------------------------
# AND Operator
# ----------------------------------------

print("AND Operator")

print(a > b and a > 5)
print(a > b and b > 20)

print()

# ----------------------------------------
# OR Operator
# ----------------------------------------

print("OR Operator")

print(a > b or b > 20)
print(a < b or b > 20)

print()

# ----------------------------------------
# NOT Operator
# ----------------------------------------

print("NOT Operator")

print(not (a > b))
print(not (a < b))

print()

print("=" * 60)
print("MORE EXAMPLES")
print("=" * 60)

age = 20

print(age >= 18 and age <= 60)

print()

marks = 75

print(marks >= 33 and marks <= 100)

print()

salary = 50000

print(salary > 30000 or salary > 100000)

print()

username = "admin"
password = "1234"

print(username == "admin" and password == "1234")

print()

rain = False

print(not rain)

print()

is_student = True
has_id = True

print(is_student and has_id)

print()

is_holiday = False
is_sunday = True

print(is_holiday or is_sunday)

print()

print("=" * 60)
print("NESTED LOGICAL CONDITIONS")
print("=" * 60)

x = 15

print(x > 10 and x < 20)
print(x < 10 or x > 20)
print(not (x == 15))

print()

print("=" * 60)
print("END OF LOGICAL OPERATORS")
print("=" * 60)