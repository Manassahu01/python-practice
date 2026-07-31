"""
=========================================================
Topic       : List Slicing
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a List
# ----------------------------------------

numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original List :", numbers)

print()

# ----------------------------------------
# Basic Slicing
# ----------------------------------------

print("numbers[1:5]  :", numbers[1:5])
print("numbers[:4]   :", numbers[:4])
print("numbers[3:]   :", numbers[3:])
print("numbers[:]    :", numbers[:])

print()

# ----------------------------------------
# Negative Slicing
# ----------------------------------------

print("numbers[-4:-1] :", numbers[-4:-1])
print("numbers[:-2]   :", numbers[:-2])
print("numbers[-3:]   :", numbers[-3:])

print()

# ----------------------------------------
# Step Slicing
# ----------------------------------------

print("numbers[::2]  :", numbers[::2])
print("numbers[1::2] :", numbers[1::2])
print("numbers[::3]  :", numbers[::3])

print()

# ----------------------------------------
# Reverse List
# ----------------------------------------

print("Reversed List :", numbers[::-1])

print()

# ----------------------------------------
# Modify Using Slicing
# ----------------------------------------

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Before :", fruits)

fruits[1:3] = ["Kiwi", "Pineapple"]

print("After  :", fruits)
