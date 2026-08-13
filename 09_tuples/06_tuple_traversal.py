"""
=========================================================
Topic       : Tuple Traversal
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
# Traversal using for Loop
# ----------------------------------------

print("Using for Loop:")

for item in numbers:
    print(item)

print()

# ----------------------------------------
# Traversal using while Loop
# ----------------------------------------

print("Using while Loop:")

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

print()

# ----------------------------------------
# Traversal using range(len())
# ----------------------------------------

print("Using range(len()):")

for i in range(len(numbers)):
    print("Index :", i, "Value :", numbers[i])

print()

# ----------------------------------------
# Traversal using enumerate()
# ----------------------------------------

print("Using enumerate():")

for index, value in enumerate(numbers):
    print("Index :", index, "Value :", value)

print()

# ----------------------------------------
# Traversing a Tuple of Strings
# ----------------------------------------

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits:")

for fruit in fruits:
    print(fruit)

print()

# ----------------------------------------
# Traversing Nested Tuples
# ----------------------------------------

students = (
    ("Manas", 85),
    ("Rahul", 78),
    ("Aman", 92)
)

print("Nested Tuple Traversal:")

for student in students:
    print(student)

print()

for name, marks in students:
    print("Name :", name)
    print("Marks:", marks)
    print("-" * 20)
