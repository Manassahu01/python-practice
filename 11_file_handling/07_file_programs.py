"""
=========================================================
Topic       : File Handling Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Create a Study File
# ----------------------------------------

with open("student_study.txt", "w") as file:
    file.write("Monday - Python - 2 hours\n")
    file.write("Tuesday - NumPy - 1.5 hours\n")
    file.write("Wednesday - Pandas - 2 hours\n")
    file.write("Thursday - SQL - 2.5 hours\n")
    file.write("Friday - Power BI - 1 hour\n")

print("Study file created successfully.")
print()

# ----------------------------------------
# Program 2 : Count Number of Lines
# ----------------------------------------

with open("student_study.txt", "r") as file:
    lines = file.readlines()

print("Total Lines :", len(lines))
print()

# ----------------------------------------
# Program 3 : Count Number of Words
# ----------------------------------------

with open("student_study.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total Words :", len(words))
print()

# ----------------------------------------
# Program 4 : Search for a Subject
# ----------------------------------------

search_subject = "Python"

if search_subject.lower() in data.lower():
    print(search_subject, "was found in the study record.")
else:
    print(search_subject, "was not found.")

print()

# ----------------------------------------
# Program 5 : Count Occurrences of a Word
# ----------------------------------------

subject = "Python"
count = data.lower().count(subject.lower())

print(subject, "appears", count, "time(s).")
print()

# ----------------------------------------
# Program 6 : Display Each Study Record
# ----------------------------------------

print("Study Records:")

with open("student_study.txt", "r") as file:
    for line in file:
        print(line.strip())

print()

# ----------------------------------------
# Program 7 : Calculate Total Study Hours
# ----------------------------------------

total_hours = 0

with open("student_study.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" - ")
        hours_text = parts[2]
        hours = float(hours_text.split()[0])
        total_hours += hours

print("Total Study Hours :", total_hours)
print()

# ----------------------------------------
# Program 8 : Find the Longest Record
# ----------------------------------------

longest_record = ""

with open("student_study.txt", "r") as file:
    for line in file:
        line = line.strip()

        if len(line) > len(longest_record):
            longest_record = line

print("Longest Record :", longest_record)
print()

# ----------------------------------------
# Program 9 : Copy File Content
# ----------------------------------------

with open("student_study.txt", "r") as source:
    data = source.read()

with open("student_study_backup.txt", "w") as backup:
    backup.write(data)

print("Backup file created successfully.")
