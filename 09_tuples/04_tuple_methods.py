"""
=========================================================
Topic       : Tuple Methods
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Create a Tuple
numbers = (10, 20, 10, 30, 40, 10, 50)

print("Tuple :", numbers)
print()

# count()
print("Count of 10 :", numbers.count(10))
print("Count of 20 :", numbers.count(20))
print("Count of 100:", numbers.count(100))
print()

# index()
print("Index of 30 :", numbers.index(30))
print("Index of 50 :", numbers.index(50))
print()

# count() with Strings
fruits = ("Apple", "Banana", "Apple", "Mango", "Apple")

print("Apple Count :", fruits.count("Apple"))
print("Mango Count :", fruits.count("Mango"))
print()

# index() with Strings
print("Index of Banana :", fruits.index("Banana"))
print("Index of Mango  :", fruits.index("Mango"))
print()

# Tuple Methods
print("Available Tuple Methods:")
print("1. count()")
print("2. index()")

# Tuples have only two built-in methods:
# count() and index()
# because tuples are immutable.
