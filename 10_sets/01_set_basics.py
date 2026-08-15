"""
=========================================================
Topic       : Set Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Creating a Set
numbers = {10, 20, 30, 40, 50}
print("Numbers Set :", numbers)
print()

# Set with Duplicate Values
duplicate = {10, 20, 10, 30, 20, 40}
print("Set with Duplicates :", duplicate)
print()

# Set with Different Data Types
data = {10, 25.5, "Python", True}
print("Mixed Set :", data)
print()

# Empty Set
empty_set = set()
print("Empty Set :", empty_set)
print("Type :", type(empty_set))
print()

# Creating Set using set()
fruits = set(["Apple", "Banana", "Mango"])
print("Fruits Set :", fruits)
print()

# Length of Set
print("Length :", len(numbers))
print()

# Type of Set
print("Type :", type(numbers))
print()

# Important: {} creates an Empty Dictionary
empty = {}
print("Type of {} :", type(empty))

# To create an empty set, use set()
