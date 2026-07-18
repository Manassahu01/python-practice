"""
=========================================================
Topic       : String Indexing in Python
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
Indexing is used to access individual characters in a string.

Python supports two types of indexing:

1. Positive Indexing
   Starts from 0 (Left to Right)

2. Negative Indexing
   Starts from -1 (Right to Left)

Example:

String : P Y T H O N
Index  : 0 1 2 3 4 5
Neg Id : -6 -5 -4 -3 -2 -1
"""

print("=" * 60)
print("STRING INDEXING")
print("=" * 60)

text = "Python"

print("String :", text)
print()

print("Positive Indexing")
for i in range(len(text)):
    print(text[i])

print()

print("Negative Indexing")
for i in range(-1, -len(text)-1, -1):
    print(text[i])

print()

language = "Programming"
print("First Character :", language[0])
print("Last Character :", language[-1])

print()

word = "Python"
middle_index = len(word) // 2
print("Middle Character :", word[middle_index])

print()

city = "Bhopal"
index = 3
print(city[index])

print()

name = "Manas"
for i in range(len(name)):
    print(f"Index {i} -> {name[i]}")

print()

print("Valid Index :", text[2])
# print(text[10])  # Uncomment to see IndexError

print()
print("Length of String :", len(text))

print()
print("=" * 60)
print("END OF STRING INDEXING")
print("=" * 60)
