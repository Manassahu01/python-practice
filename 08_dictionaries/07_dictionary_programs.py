"""
=========================================================
Topic       : Dictionary Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Find Maximum Value
# ----------------------------------------

marks = {
    "Manas": 85,
    "Rahul": 78,
    "Aman": 92,
    "Priya": 88
}

print("Maximum Marks :", max(marks.values()))

print()

# ----------------------------------------
# Program 2 : Find Minimum Value
# ----------------------------------------

print("Minimum Marks :", min(marks.values()))

print()

# ----------------------------------------
# Program 3 : Find Student with Highest Marks
# ----------------------------------------

highest_student = max(marks, key=marks.get)

print("Highest Scorer :", highest_student)
print("Marks :", marks[highest_student])

print()

# ----------------------------------------
# Program 4 : Calculate Total Marks
# ----------------------------------------

print("Total Marks :", sum(marks.values()))

print()

# ----------------------------------------
# Program 5 : Calculate Average Marks
# ----------------------------------------

average = sum(marks.values()) / len(marks)

print("Average Marks :", average)

print()

# ----------------------------------------
# Program 6 : Search Student
# ----------------------------------------

name = "Manas"

if name in marks:
    print(name, "found.")
else:
    print(name, "not found.")

print()

# ----------------------------------------
# Program 7 : Count Even and Odd Values
# ----------------------------------------

numbers = {
    "a": 10,
    "b": 21,
    "c": 34,
    "d": 45,
    "e": 50
}

even = 0
odd = 0

for value in numbers.values():
    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Values :", even)
print("Odd Values  :", odd)

print()

# ----------------------------------------
# Program 8 : Merge Two Dictionaries
# ----------------------------------------

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1.copy()
merged.update(dict2)

print("Merged Dictionary :", merged)
