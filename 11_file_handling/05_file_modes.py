"""
=========================================================
Topic       : File Modes
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Real-Life Example:
# A student maintains a study log using different file modes.

# ----------------------------------------
# 1. Write Mode (w)
# ----------------------------------------

with open("study_modes.txt", "w") as file:
    file.write("Python - 2 hours\n")
    file.write("NumPy - 1 hour\n")

print("Write mode: File created/overwritten.")
print()

# ----------------------------------------
# 2. Read Mode (r)
# ----------------------------------------

with open("study_modes.txt", "r") as file:
    data = file.read()

print("Read mode:")
print(data)
print()

# ----------------------------------------
# 3. Append Mode (a)
# ----------------------------------------

with open("study_modes.txt", "a") as file:
    file.write("Pandas - 2 hours\n")

print("Append mode: New record added.")
print()

# ----------------------------------------
# 4. Read and Write Mode (r+)
# ----------------------------------------

with open("study_modes.txt", "r+") as file:
    data = file.read()

    print("r+ mode - Existing Data:")
    print(data)

    file.write("SQL - 2 hours\n")

print("r+ mode: File can be read and written.")
print()

# ----------------------------------------
# 5. Write and Read Mode (w+)
# ----------------------------------------

with open("new_study_log.txt", "w+") as file:
    file.write("Machine Learning - 2 hours\n")

    # Move cursor to the beginning
    file.seek(0)

    data = file.read()

print("w+ mode:")
print(data)
print()

# ----------------------------------------
# 6. Append and Read Mode (a+)
# ----------------------------------------

with open("study_modes.txt", "a+") as file:
    file.write("Power BI - 1.5 hours\n")

    # Move cursor to the beginning
    file.seek(0)

    data = file.read()

print("a+ mode:")
print(data)
print()

# ----------------------------------------
# File Mode Summary
# ----------------------------------------

print("File Mode Summary:")
print("r  -> Read")
print("w  -> Write / Overwrite")
print("a  -> Append")
print("r+ -> Read and Write")
print("w+ -> Write and Read")
print("a+ -> Append and Read")
