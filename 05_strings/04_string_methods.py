"""
=========================================================
Topic       : String Methods in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
String methods are built-in functions used to perform
different operations on strings.

Strings are immutable, so these methods return a new string.
"""

print("=" * 60)
print("STRING METHODS")
print("=" * 60)

text = "python programming"

print("Original :", text)
print("upper()      :", text.upper())
print("lower()      :", text.lower())
print("title()      :", text.title())
print("capitalize() :", text.capitalize())
print("swapcase()   :", text.swapcase())

print()

name = "   Manas Sahu   "

print("strip()  :", name.strip())
print("lstrip() :", name.lstrip())
print("rstrip() :", name.rstrip())

print()

sentence = "I love Python"

print("replace() :", sentence.replace("Python", "Data Science"))

print()

languages = "Python,Java,C++,SQL"

print("split() :", languages.split(","))

print()

words = ["Python", "is", "Awesome"]

print("join() :", " ".join(words))

print()

course = "Python Programming"

print("find('Python') :", course.find("Python"))
print("find('Java')   :", course.find("Java"))
print("index('Programming') :", course.index("Programming"))

print()

message = "banana"

print("count('a') :", message.count("a"))

print()

website = "https://github.com"

print("startswith('https') :", website.startswith("https"))
print("endswith('.com')    :", website.endswith(".com"))

print()

a = "Python"
b = "Python123"
c = "12345"
d = "Python 3"
e = "     "

print("isalpha() :", a.isalpha())
print("isalnum() :", b.isalnum())
print("isdigit() :", c.isdigit())
print("isspace() :", e.isspace())

print()

print("=" * 60)
print("END OF STRING METHODS")
print("=" * 60)
