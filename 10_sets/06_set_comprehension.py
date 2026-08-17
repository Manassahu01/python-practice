"""
=========================================================
Topic       : Set Comprehension
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Basic Set Comprehension
numbers = [1, 2, 3, 4, 5]

squares = {x ** 2 for x in numbers}

print("Squares Set :", squares)
print()

# Even Numbers
even_numbers = {x for x in numbers if x % 2 == 0}

print("Even Numbers :", even_numbers)
print()

# Odd Numbers
odd_numbers = {x for x in numbers if x % 2 != 0}

print("Odd Numbers :", odd_numbers)
print()

# Set Comprehension with if-else
result = {
    "Even" if x % 2 == 0 else "Odd"
    for x in numbers
}

print("Result :", result)
print()

# Convert Strings to Uppercase
fruits = ["apple", "banana", "mango", "apple"]

upper_fruits = {fruit.upper() for fruit in fruits}

print("Uppercase Fruits :", upper_fruits)
print()

# Find Unique Characters
word = "programming"

unique_characters = {char for char in word}

print("Unique Characters :", unique_characters)
print()

# Set Comprehension with Condition
numbers = range(1, 11)

multiples_of_three = {x for x in numbers if x % 3 == 0}

print("Multiples of 3 :", multiples_of_three)
print()

# Remove Duplicates
data = [10, 20, 10, 30, 20, 40, 30]

unique_data = {x for x in data}

print("Original Data :", data)
print("Unique Data   :", unique_data)
