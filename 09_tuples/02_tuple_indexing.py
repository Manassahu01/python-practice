"""
=========================================================
Topic       : Tuple Indexing
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a Tuple
# ----------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Tuple :", numbers)

print()

# ----------------------------------------
# Positive Indexing
# ----------------------------------------

print("First Element :", numbers[0])
print("Third Element :", numbers[2])
print("Last Element  :", numbers[4])

print()

# ----------------------------------------
# Negative Indexing
# ----------------------------------------

print("Last Element        :", numbers[-1])
print("Second Last Element :", numbers[-2])
print("Third Last Element  :", numbers[-3])

print()

# ----------------------------------------
# Access Different Data Types
# ----------------------------------------

data = (100, "Python", 45.5, True)

print("Integer :", data[0])
print("String  :", data[1])
print("Float   :", data[2])
print("Boolean :", data[3])

print()

# ----------------------------------------
# Indexing with a Single Element Tuple
# ----------------------------------------

single = ("Python",)

print("Single Element :", single[0])

print()

# ----------------------------------------
# Find Index of an Element
# ----------------------------------------

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Index of Mango :", fruits.index("Mango"))
