"""
=========================================================
Topic       : Dictionary Practice Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Reverse Key-Value Pairs
# ----------------------------------------

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

reversed_dict = {value: key for key, value in data.items()}

print("Original :", data)
print("Reversed :", reversed_dict)

print()

# ----------------------------------------
# Program 2 : Remove a Key
# ----------------------------------------

student = {
    "name": "Manas",
    "age": 20,
    "course": "BCA"
}

student.pop("age")

print("After Removing Age :", student)

print()

# ----------------------------------------
# Program 3 : Add a New Key-Value Pair
# ----------------------------------------

student["city"] = "Bhilai"

print("After Adding City :", student)

print()

# ----------------------------------------
# Program 4 : Find Keys with Values Greater Than 50
# ----------------------------------------

marks = {
    "Math": 78,
    "English": 45,
    "Python": 92,
    "SQL": 38,
    "Statistics": 65
}

result = {
    subject: score
    for subject, score in marks.items()
    if score > 50
}

print("Marks Greater Than 50 :", result)

print()

# ----------------------------------------
# Program 5 : Count Frequency of Characters
# ----------------------------------------

word = "python"

frequency = {}

for char in word:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency :", frequency)

print()

# ----------------------------------------
# Program 6 : Find Common Keys
# ----------------------------------------

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common Keys :", common_keys)

print()

# ----------------------------------------
# Program 7 : Merge Dictionaries
# ----------------------------------------

first = {"a": 1, "b": 2}
second = {"c": 3, "d": 4}

merged = {**first, **second}

print("Merged Dictionary :", merged)

print()

# ----------------------------------------
# Program 8 : Find Highest Value
# ----------------------------------------

scores = {
    "Python": 85,
    "SQL": 91,
    "Excel": 78,
    "Power BI": 88
}

highest_subject = max(scores, key=scores.get)

print("Highest Score Subject :", highest_subject)
print("Score :", scores[highest_subject])

print()

# ----------------------------------------
# Program 9 : Check Empty Dictionary
# ----------------------------------------

empty = {}

if not empty:
    print("Dictionary is Empty.")
else:
    print("Dictionary is Not Empty.")

print()

# ----------------------------------------
# Program 10 : Calculate Total of Values
# ----------------------------------------

prices = {
    "Pen": 20,
    "Notebook": 80,
    "Bag": 500,
    "Bottle": 150
}

total = sum(prices.values())

print("Total Price :", total)
