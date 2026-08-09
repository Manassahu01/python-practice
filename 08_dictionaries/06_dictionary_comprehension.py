"""
=========================================================
Topic       : Dictionary Comprehension
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Basic Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

squares = {x: x ** 2 for x in numbers}
print("Squares Dictionary :", squares)
print()

# Create Dictionary from Two Lists
keys = ["name", "age", "course"]
values = ["Manas", 20, "BCA"]

student = {key: value for key, value in zip(keys, values)}
print("Student Dictionary :", student)
print()

# Dictionary Comprehension with Condition
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print("Even Squares :", even_squares)
print()

# Create Dictionary of Even Numbers
even_numbers = {x: x for x in numbers if x % 2 == 0}
print("Even Numbers :", even_numbers)
print()

# Convert Values to Uppercase
fruits = ["apple", "banana", "mango"]

fruit_dict = {fruit: fruit.upper() for fruit in fruits}
print("Fruit Dictionary :", fruit_dict)
print()

# Dictionary Comprehension with if-else
result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in numbers
}

print("Result :", result)
print()

# Create Dictionary from a String
word = "PYTHON"

letters = {letter: ord(letter) for letter in word}
print("ASCII Dictionary :", letters)
