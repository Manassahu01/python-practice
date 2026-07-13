"""
=========================================================
Topic       : While Loop in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
A while loop executes a block of code repeatedly as long
as the given condition is True.

Syntax:

while condition:
    statement
"""

print("=" * 60)
print("WHILE LOOP")
print("=" * 60)

# ----------------------------------------
# Example 1
# Print numbers from 1 to 5
# ----------------------------------------

i = 1

while i <= 5:
    print(i)
    i += 1

print()

# ----------------------------------------
# Example 2
# Print numbers from 5 to 1
# ----------------------------------------

i = 5

while i >= 1:
    print(i)
    i -= 1

print()

# ----------------------------------------
# Example 3
# Print Even Numbers
# ----------------------------------------

i = 2

while i <= 10:
    print(i)
    i += 2

print()

# ----------------------------------------
# Example 4
# Print Odd Numbers
# ----------------------------------------

i = 1

while i <= 10:
    print(i)
    i += 2

print()

# ----------------------------------------
# Example 5
# Sum of First 10 Numbers
# ----------------------------------------

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)

print()

# ----------------------------------------
# Example 6
# Multiplication Table of 5
# ----------------------------------------

i = 1

while i <= 10:
    print(f"5 x {i} = {5 * i}")
    i += 1

print()

# ----------------------------------------
# Example 7
# Reverse Counting
# ----------------------------------------

i = 10

while i >= 1:
    print(i)
    i -= 1

print()

print("=" * 60)
print("BREAK")
print("=" * 60)

i = 1

while i <= 10:
    if i == 6:
        break

    print(i)
    i += 1

print()

print("=" * 60)
print("CONTINUE")
print("=" * 60)

i = 0

while i < 10:
    i += 1

    if i == 6:
        continue

    print(i)

print()

print("=" * 60)
print("PASS")
print("=" * 60)

i = 1

while i <= 5:

    if i == 3:
        pass

    print(i)

    i += 1

print()

print("=" * 60)
print("END OF WHILE LOOP")
print("=" * 60)