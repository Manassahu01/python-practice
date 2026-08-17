"""
=========================================================
Topic       : Set Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Remove Duplicate Values
# ----------------------------------------

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print("Original List :", numbers)
print("Unique Values :", unique_numbers)

print()

# ----------------------------------------
# Program 2 : Find Common Elements
# ----------------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

print("Common Elements :", common)

print()

# ----------------------------------------
# Program 3 : Find Unique Elements
# ----------------------------------------

unique = set1.difference(set2)

print("Elements only in Set 1 :", unique)

print()

# ----------------------------------------
# Program 4 : Find Union of Two Sets
# ----------------------------------------

combined = set1.union(set2)

print("Combined Set :", combined)

print()

# ----------------------------------------
# Program 5 : Check Membership
# ----------------------------------------

value = 3

if value in set1:
    print(value, "is present in Set 1.")
else:
    print(value, "is not present in Set 1.")

print()

# ----------------------------------------
# Program 6 : Find Even and Odd Numbers
# ----------------------------------------

numbers = {10, 21, 32, 43, 54, 65}

even = set()
odd = set()

for number in numbers:
    if number % 2 == 0:
        even.add(number)
    else:
        odd.add(number)

print("Even Numbers :", even)
print("Odd Numbers  :", odd)

print()

# ----------------------------------------
# Program 7 : Find Maximum and Minimum
# ----------------------------------------

scores = {78, 85, 92, 67, 88}

print("Maximum :", max(scores))
print("Minimum :", min(scores))

print()

# ----------------------------------------
# Program 8 : Find Students Present in Both Classes
# ----------------------------------------

class_a = {"Manas", "Rahul", "Aman", "Priya"}
class_b = {"Aman", "Priya", "Rohit", "Neha"}

both_classes = class_a & class_b

print("Students in Both Classes :", both_classes)

print()

# ----------------------------------------
# Program 9 : Check Subset
# ----------------------------------------

required_skills = {"Python", "SQL"}
student_skills = {"Python", "SQL", "Excel", "Power BI"}

if required_skills.issubset(student_skills):
    print("Student has all required skills.")
else:
    print("Student does not have all required skills.")

print()

# ----------------------------------------
# Program 10 : Find Total Unique Characters
# ----------------------------------------

word = "programming"

characters = set(word)

print("Unique Characters :", characters)
print("Total Unique Characters :", len(characters))
