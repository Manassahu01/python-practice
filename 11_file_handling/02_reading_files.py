"""
=========================================================
Topic       : Reading Files
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Real-Life Example:
# A student stores daily study records in a text file.

# ----------------------------------------
# Step 1 : Create Sample Study Record
# ----------------------------------------

with open("study_record.txt", "w") as file:
    file.write("Monday - Python - 2 hours\n")
    file.write("Tuesday - NumPy - 1.5 hours\n")
    file.write("Wednesday - Pandas - 2 hours\n")
    file.write("Thursday - SQL - 2.5 hours\n")

print("Study record created successfully.")
print()

# ----------------------------------------
# Step 2 : Read the Complete File
# ----------------------------------------

with open("study_record.txt", "r") as file:
    data = file.read()

print("Using read():")
print(data)
print()

# ----------------------------------------
# Step 3 : Read One Line
# ----------------------------------------

with open("study_record.txt", "r") as file:
    first_line = file.readline()

print("Using readline():")
print(first_line)
print()

# ----------------------------------------
# Step 4 : Read All Lines
# ----------------------------------------

with open("study_record.txt", "r") as file:
    lines = file.readlines()

print("Using readlines():")

for line in lines:
    print(line.strip())

print()

# ----------------------------------------
# Step 5 : Count Study Records
# ----------------------------------------

print("Total Study Records :", len(lines))
