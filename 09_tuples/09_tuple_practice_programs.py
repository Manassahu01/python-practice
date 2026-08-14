"""
=========================================================
Topic       : Tuple Practice Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Count Occurrences
# ----------------------------------------

numbers = (10, 20, 10, 30, 10, 40)

print("Count of 10 :", numbers.count(10))

print()

# ----------------------------------------
# Program 2 : Find Index of an Element
# ----------------------------------------

print("Index of 30 :", numbers.index(30))

print()

# ----------------------------------------
# Program 3 : Check if Tuple is Empty
# ----------------------------------------

empty_tuple = ()

if not empty_tuple:
    print("Tuple is Empty.")
else:
    print("Tuple is Not Empty.")

print()

# ----------------------------------------
# Program 4 : Find Second Largest Element
# ----------------------------------------

values = (12, 45, 7, 89, 34)

sorted_values = sorted(values)

print("Second Largest :", sorted_values[-2])

print()

# ----------------------------------------
# Program 5 : Find Common Elements
# ----------------------------------------

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7)

common = ()

for item in tuple1:
    if item in tuple2:
        common += (item,)

print("Common Elements :", common)

print()

# ----------------------------------------
# Program 6 : Convert List to Tuple
# ----------------------------------------

numbers_list = [10, 20, 30, 40]

numbers_tuple = tuple(numbers_list)

print("List  :", numbers_list)
print("Tuple :", numbers_tuple)

print()

# ----------------------------------------
# Program 7 : Convert Tuple to List
# ----------------------------------------

data = ("Python", "NumPy", "Pandas")

data_list = list(data)

print("Tuple :", data)
print("List  :", data_list)

print()

# ----------------------------------------
# Program 8 : Find Length of Nested Tuple
# ----------------------------------------

students = (
    ("Manas", 85),
    ("Rahul", 78),
    ("Aman", 92)
)

print("Number of Students :", len(students))

print()

# ----------------------------------------
# Program 9 : Calculate Total Marks
# ----------------------------------------

marks = (78, 85, 92, 67, 88)

print("Total Marks :", sum(marks))

print()

# ----------------------------------------
# Program 10 : Find Values Above Average
# ----------------------------------------

average = sum(marks) / len(marks)

above_average = tuple(mark for mark in marks if mark > average)

print("Average Marks :", average)
print("Above Average :", above_average)
