"""
=========================================================
Topic       : String Slicing in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
String slicing is used to extract a part of a string.

Syntax:
string[start:stop:step]

start -> inclusive
stop  -> exclusive
step  -> increment/decrement
"""

print("=" * 60)
print("STRING SLICING")
print("=" * 60)

text = "Python Programming"

print("Original String :", text)
print()

print("First 6 Characters :", text[0:6])
print("Programming :", text[7:])
print("First 10 Characters :", text[:10])
print("Complete String :", text[:])

print()

print("Every Second Character :", text[::2])
print("Every Third Character :", text[::3])

print()

print("Reverse String :", text[::-1])

print()

word = "Programming"

print("First Character :", word[0])
print("Last Character :", word[-1])
print("Last 5 Characters :", word[-5:])
print("Without First Character :", word[1:])
print("Without Last Character :", word[:-1])

print()

name = "Manas Sahu"

print("First Name :", name[:5])
print("Last Name :", name[6:])

print()

course = "Data Science"

print(course[0:4])
print(course[5:])
print(course[::-1])

print()

print("=" * 60)
print("END OF STRING SLICING")
print("=" * 60)
