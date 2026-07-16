"""
=========================================================
Topic       : String Basics in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
A string is a sequence of characters enclosed in
single quotes (' '), double quotes (" "), or
triple quotes (''' ''' or \"\"\" \"\"\").

Strings are:
1. Ordered
2. Immutable
3. Iterable
"""

print("=" * 60)
print("STRING BASICS")
print("=" * 60)

# ----------------------------------------
# Creating Strings
# ----------------------------------------

name = "Manas"
course = 'Python Programming'
college = """KK Modi University"""

print(name)
print(course)
print(college)

print()

# ----------------------------------------
# Data Type of String
# ----------------------------------------

language = "Python"

print(language)
print(type(language))

print()

# ----------------------------------------
# Empty String
# ----------------------------------------

text = ""

print(text)
print(type(text))

print()

# ----------------------------------------
# String Length
# ----------------------------------------

message = "Welcome to Python"

print(message)
print("Length:", len(message))

print()

# ----------------------------------------
# String Concatenation
# ----------------------------------------

first_name = "Manas"
last_name = "Sahu"

full_name = first_name + " " + last_name

print(full_name)

print()

# ----------------------------------------
# String Repetition
# ----------------------------------------

word = "Python "

print(word * 3)

print()

# ----------------------------------------
# Escape Characters
# ----------------------------------------

print("Hello\nWorld")
print("Python\tProgramming")
print("She said, \"Hello!\"")
print('It\'s Python.')

print()

# ----------------------------------------
# Multiline String
# ----------------------------------------

paragraph = """
Python is an easy-to-learn
and powerful programming language.
"""

print(paragraph)

print()

# ----------------------------------------
# Checking Membership
# ----------------------------------------

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print()

# ----------------------------------------
# Comparing Strings
# ----------------------------------------

a = "Python"
b = "Python"
c = "Java"

print(a == b)
print(a == c)

print()

# ----------------------------------------
# Iterating Through a String
# ----------------------------------------

name = "Python"

for ch in name:
    print(ch)

print()

# ----------------------------------------
# Useful Built-in Functions
# ----------------------------------------

text = "Data Science"

print("Length :", len(text))
print("Maximum Character :", max(text))
print("Minimum Character :", min(text))

print()

# ----------------------------------------
# String Immutability
# ----------------------------------------

message = "Python"

print(message)

# Strings are immutable.
# The following line will generate an error.

# message[0] = "J"

print("Strings are Immutable.")

print()

print("=" * 60)
print("END OF STRING BASICS")
print("=" * 60)