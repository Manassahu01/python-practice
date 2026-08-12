"""
=========================================================
Topic       : Tuple Slicing
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Create a Tuple
numbers = (10, 20, 30, 40, 50, 60, 70)

print("Original Tuple :", numbers)
print()

# Basic Slicing
print("numbers[1:5] :", numbers[1:5])
print("numbers[:4]  :", numbers[:4])
print("numbers[3:]  :", numbers[3:])
print("numbers[:]   :", numbers[:])
print()

# Negative Slicing
print("numbers[-4:-1] :", numbers[-4:-1])
print("numbers[:-2]   :", numbers[:-2])
print("numbers[-3:]   :", numbers[-3:])
print()

# Step Slicing
print("numbers[::2]  :", numbers[::2])
print("numbers[1::2] :", numbers[1::2])
print("numbers[::3]  :", numbers[::3])
print()

# Reverse Tuple
print("Reversed Tuple :", numbers[::-1])
print()

# Slicing Tuple with Different Data Types
data = (10, "Python", 25.5, True, "NumPy")
print("Sliced Data :", data[1:4])
