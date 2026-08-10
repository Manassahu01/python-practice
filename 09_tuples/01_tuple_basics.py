"""
=========================================================
Topic       : Tuple Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Creating a Tuple
numbers = (10, 20, 30, 40, 50)
print("Numbers Tuple :", numbers)
print()

# Tuple with Different Data Types
data = (10, 25.5, "Python", True)
print("Mixed Tuple :", data)
print()

# Empty Tuple
empty_tuple = ()
print("Empty Tuple :", empty_tuple)
print()

# Single Element Tuple
single_tuple = (10,)
print("Single Element Tuple :", single_tuple)
print("Type :", type(single_tuple))
print()

# Creating Tuple using tuple()
fruits = tuple(["Apple", "Banana", "Mango"])
print("Fruits Tuple :", fruits)
print()

# Duplicate Values
duplicate = (10, 20, 10, 30, 20)
print("Duplicate Tuple :", duplicate)
print()

# Length of Tuple
print("Length :", len(numbers))
print()

# Type of Tuple
print("Type :", type(numbers))
print()

# Tuple is Immutable
# numbers[0] = 100
# This gives TypeError because tuples cannot be modified.
