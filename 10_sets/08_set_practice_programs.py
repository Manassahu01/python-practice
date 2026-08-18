"""
=========================================================
Topic       : Set Practice Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Remove Duplicates from a List
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

print("Common Elements :", set1 & set2)

print()

# ----------------------------------------
# Program 3 : Find Elements Only in Set 1
# ----------------------------------------

print("Only in Set 1 :", set1 - set2)

print()

# ----------------------------------------
# Program 4 : Find Elements Only in Set 2
# ----------------------------------------

print("Only in Set 2 :", set2 - set1)

print()

# ----------------------------------------
# Program 5 : Find Elements in Either Set
# ----------------------------------------

print("Union :", set1 | set2)

print()

# ----------------------------------------
# Program 6 : Find Elements in Exactly One Set
# ----------------------------------------

print("Symmetric Difference :", set1 ^ set2)

print()

# ----------------------------------------
# Program 7 : Check Subset and Superset
# ----------------------------------------

small_set = {1, 2}
large_set = {1, 2, 3, 4, 5}

print("Is Subset :", small_set.issubset(large_set))
print("Is Superset :", large_set.issuperset(small_set))

print()

# ----------------------------------------
# Program 8 : Separate Even and Odd Numbers
# ----------------------------------------

numbers = {10, 15, 20, 25, 30, 35}

even = {number for number in numbers if number % 2 == 0}
odd = {number for number in numbers if number % 2 != 0}

print("Even Numbers :", even)
print("Odd Numbers  :", odd)

print()

# ----------------------------------------
# Program 9 : Find Unique Characters
# ----------------------------------------

word = "programming"

unique_characters = set(word)

print("Unique Characters :", unique_characters)
print("Number of Unique Characters :", len(unique_characters))

print()

# ----------------------------------------
# Program 10 : Check if Two Sets are Disjoint
# ----------------------------------------

a = {1, 2, 3}
b = {4, 5, 6}

print("Are Sets Disjoint :", a.isdisjoint(b))

print()

# ----------------------------------------
# Program 11 : Find Maximum and Minimum
# ----------------------------------------

scores = {78, 85, 92, 67, 88}

print("Maximum Score :", max(scores))
print("Minimum Score :", min(scores))

print()

# ----------------------------------------
# Program 12 : Find Students in Both Courses
# ----------------------------------------

python_students = {"Manas", "Rahul", "Aman", "Priya"}
sql_students = {"Aman", "Priya", "Rohit", "Neha"}

both_courses = python_students & sql_students

print("Students in Both Courses :", both_courses)
