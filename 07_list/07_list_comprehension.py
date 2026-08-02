"""
=========================================================
Topic       : List Comprehension
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Basic List Comprehension
# ----------------------------------------

numbers = [1, 2, 3, 4, 5]

new_list = [x for x in numbers]

print("Original List :", numbers)
print("New List      :", new_list)

print()

# ----------------------------------------
# Square of Numbers
# ----------------------------------------

square = [x ** 2 for x in numbers]

print("Square List :", square)

print()

# ----------------------------------------
# Even Numbers
# ----------------------------------------

even = [x for x in numbers if x % 2 == 0]

print("Even Numbers :", even)

print()

# ----------------------------------------
# Odd Numbers
# ----------------------------------------

odd = [x for x in numbers if x % 2 != 0]

print("Odd Numbers :", odd)

print()

# ----------------------------------------
# Convert Strings to Uppercase
# ----------------------------------------

fruits = ["apple", "banana", "mango"]

upper_fruits = [fruit.upper() for fruit in fruits]

print("Uppercase List :", upper_fruits)

print()

# ----------------------------------------
# List Comprehension with if-else
# ----------------------------------------

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)

print()

# ----------------------------------------
# Nested List Comprehension
# ----------------------------------------

matrix = [[1, 2], [3, 4], [5, 6]]

flatten = [item for row in matrix for item in row]

print("Flatten List :", flatten)
