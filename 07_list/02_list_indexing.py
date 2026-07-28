"""
=========================================================
Topic       : List Indexing
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Positive Indexing
# ----------------------------------------

numbers = [10, 20, 30, 40, 50]

print("List :", numbers)
print("First Element  :", numbers[0])
print("Third Element  :", numbers[2])
print("Last Element   :", numbers[4])

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

data = [100, "Python", 45.6, True]

print(data[0])
print(data[1])
print(data[2])
print(data[3])

print()

# ----------------------------------------
# Modify List Element
# ----------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("Before :", fruits)

fruits[1] = "Orange"

print("After  :", fruits)

print()

# ----------------------------------------
# User Defined List
# ----------------------------------------

marks = [85, 90, 78, 92, 88]

print("First Mark :", marks[0])
print("Last Mark  :", marks[-1])
