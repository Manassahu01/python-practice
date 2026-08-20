"""
=========================================================
Topic       : with Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Real-Life Example:
A student maintains a study report. The `with open()`
statement is used so Python automatically closes the file
after the work is completed.
"""

# ----------------------------------------
# Step 1 : Write a Study Report
# ----------------------------------------

with open("study_report.txt", "w") as file:
    file.write("Student Study Report\n")
    file.write("--------------------\n")
    file.write("Python: 2 hours\n")
    file.write("NumPy: 1.5 hours\n")
    file.write("Pandas: 2 hours\n")

print("Study report created successfully.")

print()

# ----------------------------------------
# Step 2 : Read the File
# ----------------------------------------

with open("study_report.txt", "r") as file:
    data = file.read()

print("Study Report:")
print(data)

print()

# ----------------------------------------
# Step 3 : Check if File is Closed
# ----------------------------------------

print("Is file closed after 'with' block?", file.closed)

print()

# ----------------------------------------
# Step 4 : Append New Data
# ----------------------------------------

with open("study_report.txt", "a") as file:
    file.write("SQL: 2 hours\n")
    file.write("Power BI: 1 hour\n")

print("New study records added.")

print()

# ----------------------------------------
# Step 5 : Read Updated Report
# ----------------------------------------

with open("study_report.txt", "r") as file:
    updated_data = file.read()

print("Updated Study Report:")
print(updated_data)

# ----------------------------------------
# Important Note
# ----------------------------------------
# The with statement automatically closes the file
# when the block finishes.
#
# This is safer and cleaner than:
#
# file = open("study_report.txt", "r")
# data = file.read()
# file.close()
