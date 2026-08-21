"""
=========================================================
Topic       : File Handling Practice Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Create a Simple Notes File
# ----------------------------------------

with open("notes.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("Practice makes programming better.\n")

print("Notes file created.")
print()

# ----------------------------------------
# Program 2 : Count Lines in a File
# ----------------------------------------

with open("notes.txt", "r") as file:
    lines = file.readlines()

print("Total Lines :", len(lines))
print()

# ----------------------------------------
# Program 3 : Count Words in a File
# ----------------------------------------

with open("notes.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total Words :", len(words))
print()

# ----------------------------------------
# Program 4 : Count Characters
# ----------------------------------------

print("Total Characters :", len(data))
print()

# ----------------------------------------
# Program 5 : Search for a Word
# ----------------------------------------

search_word = "Python"

if search_word.lower() in data.lower():
    print(search_word, "found in the file.")
else:
    print(search_word, "not found.")

print()

# ----------------------------------------
# Program 6 : Count a Word
# ----------------------------------------

word = "Python"

word_count = data.lower().count(word.lower())

print(word, "appears", word_count, "time(s).")
print()

# ----------------------------------------
# Program 7 : Append a New Note
# ----------------------------------------

with open("notes.txt", "a") as file:
    file.write("I am currently learning File Handling.\n")

print("New note added.")
print()

# ----------------------------------------
# Program 8 : Display File Line by Line
# ----------------------------------------

print("File Content:")

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

print()

# ----------------------------------------
# Program 9 : Copy a File
# ----------------------------------------

with open("notes.txt", "r") as source:
    content = source.read()

with open("notes_backup.txt", "w") as backup:
    backup.write(content)

print("Backup file created.")
print()

# ----------------------------------------
# Program 10 : Find the Longest Word
# ----------------------------------------

words = content.split()

longest_word = max(words, key=len)

print("Longest Word :", longest_word)
print()

# ----------------------------------------
# Program 11 : Convert File Content to
#              Uppercase
# ----------------------------------------

uppercase_content = content.upper()

with open("uppercase_notes.txt", "w") as file:
    file.write(uppercase_content)

print("Uppercase copy created.")
print()

# ----------------------------------------
# Program 12 : Add a Student Record
# ----------------------------------------

with open("students.txt", "a") as file:
    file.write("Manas, BCA, Data Analytics\n")

print("Student record added.")
