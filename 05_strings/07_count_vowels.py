"""
=========================================================
Topic       : Count Vowels in a String
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Method 1 : Using Function
# ----------------------------------------

def count_vowels():

    string = "hello"

    vowels = "aeiouAEIOU"

    count = 0

    for ch in string:

        if ch in vowels:
            count += 1

    print("Total Vowels :", count)


count_vowels()

print()

# ----------------------------------------
# Method 2 : User Input
# ----------------------------------------

string = input("Enter a String : ")

vowels = "aeiouAEIOU"

count = 0

for ch in string:

    if ch in vowels:
        count += 1

print("Total Vowels :", count)