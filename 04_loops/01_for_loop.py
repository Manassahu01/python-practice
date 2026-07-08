"""
=========================================================
Topic       : For Loop in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
A for loop is used to iterate over a sequence such as
string, list, tuple, set, dictionary or range.

Syntax:

for variable in sequence:
    statement
"""

print("=" * 60)
print("FOR LOOP")
print("=" * 60)

# ----------------------------------------
# Example 1
# ----------------------------------------

for i in range(5):
    print(i)

print()

# ----------------------------------------
# Example 2
# ----------------------------------------

for i in range(1, 6):
    print(i)

print()

# ----------------------------------------
# Example 3
# ----------------------------------------

for i in range(2, 11, 2):
    print(i)

print()

# ----------------------------------------
# Example 4
# ----------------------------------------

for i in range(10, 0, -1):
    print(i)

print()

# ----------------------------------------
# Example 5
# ----------------------------------------

name = "Python"

for ch in name:
    print(ch)

print()

# ----------------------------------------
# Example 6
# ----------------------------------------

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

print()

# ----------------------------------------
# Example 7
# ----------------------------------------

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

print()

# ----------------------------------------
# Example 8
# ----------------------------------------

total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)

print()

# ----------------------------------------
# Example 9
# ----------------------------------------

for i in range(1, 11):
    print(i, end=" ")

print("\n")

# ----------------------------------------
# Example 10
# ----------------------------------------

for i in range(1, 6):
    print(i * i)

print()

print("=" * 60)
print("BREAK")
print("=" * 60)

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print()

print("=" * 60)
print("CONTINUE")
print("=" * 60)

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

print()

print("=" * 60)
print("PASS")
print("=" * 60)

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

print()

print("=" * 60)
print("END OF FOR LOOP")
print("=" * 60)