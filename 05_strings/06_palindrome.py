"""
=========================================================
Topic       : Palindrome String
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Method 1 : Check Palindrome
# ----------------------------------------

def palindrome(string):

    reverse = string[::-1]

    if string == reverse:
        print(f"{string} is a Palindrome")
    else:
        print(f"{string} is Not a Palindrome")


palindrome("madam")
palindrome("python")

print()

# ----------------------------------------
# Method 2 : User Input
# ----------------------------------------

string = input("Enter a String : ")

reverse = string[::-1]

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")