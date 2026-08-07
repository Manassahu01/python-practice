"""
=========================================================
Topic       : Dictionary Methods
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a Dictionary
# ----------------------------------------

student = {
    "name": "Manas",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:")
print(student)

print()

# ----------------------------------------
# update()
# ----------------------------------------

student.update({"age": 21, "city": "Bhilai"})
print("After update():")
print(student)

print()

# ----------------------------------------
# pop()
# ----------------------------------------

removed = student.pop("city")
print("Removed Value :", removed)
print(student)

print()

# ----------------------------------------
# popitem()
# ----------------------------------------

item = student.popitem()
print("Removed Item :", item)
print(student)

print()

# ----------------------------------------
# setdefault()
# ----------------------------------------

student.setdefault("college", "KK Modi University")
student.setdefault("age", 25)

print("After setdefault():")
print(student)

print()

# ----------------------------------------
# copy()
# ----------------------------------------

student_copy = student.copy()

print("Copied Dictionary:")
print(student_copy)

print()

# ----------------------------------------
# fromkeys()
# ----------------------------------------

keys = ["Python", "NumPy", "Pandas"]

new_dict = dict.fromkeys(keys, "Completed")

print("Dictionary from Keys:")
print(new_dict)

print()

# ----------------------------------------
# clear()
# ----------------------------------------

temp = {"A": 1, "B": 2}

print("Before clear():", temp)

temp.clear()

print("After clear():", temp)
