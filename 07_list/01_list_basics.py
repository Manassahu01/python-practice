"""
=========================================================
Topic       : List Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Creating a List
# ----------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Numbers List :", numbers)

print()

# ----------------------------------------
# List with Different Data Types
# ----------------------------------------

data = [10, 25.5, "Python", True]

print("Mixed List :", data)

print()

# ----------------------------------------
# Empty List
# ----------------------------------------

empty_list = []

print("Empty List :", empty_list)

print()

# ----------------------------------------
# Creating List using list()
# ----------------------------------------

fruits = list(("Apple", "Banana", "Mango"))

print("Fruits :", fruits)

print()

# ----------------------------------------
# Length of List
# ----------------------------------------

print("Length of Numbers List :", len(numbers))

print()

# ----------------------------------------
# Type of List
# ----------------------------------------

print("Type :", type(numbers))

print()

# ----------------------------------------
# List can Store Duplicate Values
# ----------------------------------------

duplicate = [1, 2, 2, 3, 3, 4]

print("Duplicate List :", duplicate)

print()

# ----------------------------------------
# Nested List
# ----------------------------------------

nested = [[1, 2], [3, 4], [5, 6]]

print("Nested List :", nested)
