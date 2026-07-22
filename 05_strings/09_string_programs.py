"""
=========================================================
Topic       : String Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Count Total Characters
# ----------------------------------------

string = "Hello World"

count = 0

for ch in string:
    count += 1

print("Total Characters :", count)

print()

# ----------------------------------------
# Program 2 : Count Words
# ----------------------------------------

string = "Python is easy to learn"

words = string.split()

print("Total Words :", len(words))

print()

# ----------------------------------------
# Program 3 : Count Spaces
# ----------------------------------------

string = "Python Programming Language"

spaces = 0

for ch in string:
    if ch == " ":
        spaces += 1

print("Total Spaces :", spaces)

print()

# ----------------------------------------
# Program 4 : Count Uppercase and Lowercase
# ----------------------------------------

string = "Python Programming"

upper = 0
lower = 0

for ch in string:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

print("Uppercase Letters :", upper)
print("Lowercase Letters :", lower)

print()

# ----------------------------------------
# Program 5 : Remove Spaces
# ----------------------------------------

string = "Data Science"

result = string.replace(" ", "")

print("Original :", string)
print("Without Spaces :", result)
