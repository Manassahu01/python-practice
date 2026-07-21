"""
=========================================================
Topic       : Reverse String
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Method 1 : Reverse String Using Slicing
# ----------------------------------------

string = "hello"

reverse = ""

for i in string[::-1]:
    reverse += i

print("Original String :", string)
print("Reverse String  :", reverse)

print()

# ----------------------------------------
# Method 2 : Reverse String Using Loop
# ----------------------------------------

string = "Python"

reverse = ""

for ch in string:
    reverse = ch + reverse

print("Original String :", string)
print("Reverse String  :", reverse)

print()

# ----------------------------------------
# Method 3 : User Input
# ----------------------------------------

string = input("Enter a String : ")

reverse = ""

for i in string[::-1]:
    reverse += i

print("Reverse String :", reverse)