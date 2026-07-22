"""
=========================================================
Topic       : Count Vowels and Consonants
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Method 1 : Using Predefined String
# ----------------------------------------

string = "Hello"

vowels = 0
consonants = 0

for ch in string:

    if ch.isalpha():

        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1

print("String :", string)
print("Total Vowels      :", vowels)
print("Total Consonants  :", consonants)

print()

# ----------------------------------------
# Method 2 : Using User Input
# ----------------------------------------

string = input("Enter a String : ")

vowels = 0
consonants = 0

for ch in string:

    if ch.isalpha():

        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1

print("Total Vowels      :", vowels)
print("Total Consonants  :", consonants)
