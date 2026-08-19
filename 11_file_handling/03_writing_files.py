"""
=========================================================
Topic       : Writing Files
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Real-Life Example:
A student wants to create a simple career plan and
save it permanently in a text file.
"""

# ----------------------------------------
# Step 1 : Open File in Write Mode
# ----------------------------------------

file = open("career_plan.txt", "w")

# ----------------------------------------
# Step 2 : Write Data
# ----------------------------------------

file.write("Career Plan\n")
file.write("--------------\n")
file.write("Current Course: BCA\n")
file.write("Primary Skill: Python\n")
file.write("Next Skill: Pandas\n")
file.write("Next Goal: Data Analyst Internship\n")

# ----------------------------------------
# Step 3 : Close the File
# ----------------------------------------

file.close()

print("Career plan saved successfully.")

print()

# ----------------------------------------
# Step 4 : Read the Written Data
# ----------------------------------------

file = open("career_plan.txt", "r")

data = file.read()

print("Saved Career Plan:")
print(data)

file.close()

print("File closed successfully.")

print()

# ----------------------------------------
# Step 5 : Write Multiple Lines
# ----------------------------------------

lines = [
    "Learn NumPy\n",
    "Learn Pandas\n",
    "Practice SQL\n",
    "Build Projects\n"
]

with open("learning_plan.txt", "w") as file:
    file.writelines(lines)

print("Learning plan created successfully.")
