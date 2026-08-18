"""
=========================================================
Topic       : File Handling Basics
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Real-Life Example:
A student stores important information in a text file.
This program demonstrates how Python can create, open,
write to, read from, and close a file.
"""

# ----------------------------------------
# Step 1 : Create/Open a File
# ----------------------------------------

file = open("student_info.txt", "w")

# ----------------------------------------
# Step 2 : Write Data into the File
# ----------------------------------------

file.write("Student Name: Manas Sahu\n")
file.write("Course: BCA\n")
file.write("Department: Computer Applications\n")
file.write("Goal: Become a Data Scientist\n")

# ----------------------------------------
# Step 3 : Close the File
# ----------------------------------------

file.close()

print("Student information saved successfully.")

print()

# ----------------------------------------
# Step 4 : Open the File in Read Mode
# ----------------------------------------

file = open("student_info.txt", "r")

# ----------------------------------------
# Step 5 : Read the File
# ----------------------------------------

data = file.read()

print("Student Information:")
print(data)

# ----------------------------------------
# Step 6 : Close the File
# ----------------------------------------

file.close()

print("File closed successfully.")
