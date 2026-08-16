"""
=========================================================
Topic       : Set Traversal
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Create a Set
numbers = {10, 20, 30, 40, 50}

print("Set :", numbers)
print()

# Traversal using for Loop
print("Using for Loop:")

for item in numbers:
    print(item)

print()

# Traverse and Perform Operation
print("Squares:")

for item in numbers:
    print(item, "->", item ** 2)

print()

# Check Even and Odd Elements
even = set()
odd = set()

for item in numbers:
    if item % 2 == 0:
        even.add(item)
    else:
        odd.add(item)

print("Even Set :", even)
print("Odd Set  :", odd)
print()

# Traverse a Set of Strings
fruits = {"Apple", "Banana", "Mango", "Orange"}

print("Fruits:")

for fruit in fruits:
    print(fruit)

print()

# Traverse Set using enumerate()
print("Using enumerate():")

for index, value in enumerate(numbers):
    print("Index :", index, "Value :", value)

print()

# Note:
# Sets are unordered, so the order of elements
# should not be considered fixed.
