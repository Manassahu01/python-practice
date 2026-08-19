"""
=========================================================
Topic       : Appending Files
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Real-Life Example:
A student maintains a daily learning log. Instead of
overwriting previous entries, new learning activities
are added to the end of the file.
"""

# ----------------------------------------
# Step 1 : Create Initial Learning Log
# ----------------------------------------

with open("learning_log.txt", "w") as file:
    file.write("Monday - Python Basics - 2 hours\n")
    file.write("Tuesday - Functions - 1.5 hours\n")

print("Initial learning log created.")

print()

# ----------------------------------------
# Step 2 : Open File in Append Mode
# ----------------------------------------

with open("learning_log.txt", "a") as file:
    file.write("Wednesday - NumPy - 2 hours\n")
    file.write("Thursday - Lists and Dictionaries - 1 hour\n")

print("New learning records added.")

print()

# ----------------------------------------
# Step 3 : Append One More Record
# ----------------------------------------

with open("learning_log.txt", "a") as file:
    file.write("Friday - Tuples and Sets - 1.5 hours\n")

print("Friday record added.")

print()

# ----------------------------------------
# Step 4 : Read the Complete Log
# ----------------------------------------

with open("learning_log.txt", "r") as file:
    data = file.read()

print("Complete Learning Log:")
print(data)

# ----------------------------------------
# Important Note
# ----------------------------------------
# "a" mode adds new content at the end of the file.
# It does NOT remove the existing content.
