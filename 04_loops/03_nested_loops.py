"""
=========================================================
Topic       : Nested Loops in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
A loop inside another loop is called a Nested Loop.

Syntax:

for variable1 in sequence:
    for variable2 in sequence:
        statement

A nested loop is mainly used for:
1. Pattern Printing
2. Matrix Operations
3. Tables
4. 2D Lists
"""

print("=" * 60)
print("NESTED FOR LOOP")
print("=" * 60)

# ----------------------------------------
# Example 1
# ----------------------------------------

for i in range(3):
    for j in range(3):
        print(i, j)

print()

# ----------------------------------------
# Example 2
# ----------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

print()

# ----------------------------------------
# Example 3
# ----------------------------------------

for i in range(1, 4):
    for j in range(1, 6):
        print("*", end=" ")
    print()

print()

# ----------------------------------------
# Example 4
# ----------------------------------------

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

print("=" * 60)
print("NESTED WHILE LOOP")
print("=" * 60)

i = 1

while i <= 3:

    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1

print()

# ----------------------------------------
# Example 5
# ----------------------------------------

i = 1

while i <= 3:

    j = 1

    while j <= 5:
        print("*", end=" ")

        j += 1

    print()

    i += 1

print()

print("=" * 60)
print("MULTIPLICATION TABLE (1 TO 5)")
print("=" * 60)

for i in range(1, 6):

    for j in range(1, 11):

        print(f"{i} x {j} = {i*j}")

    print()

print("=" * 60)
print("END OF NESTED LOOPS")
print("=" * 60)