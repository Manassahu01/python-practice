"""
=========================================================
Topic       : List Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Program 1 : Find Largest Element
numbers = [12, 45, 7, 89, 34]
print("Largest Element :", max(numbers))
print()

# Program 2 : Find Smallest Element
print("Smallest Element :", min(numbers))
print()

# Program 3 : Sum of All Elements
print("Sum :", sum(numbers))
print()

# Program 4 : Average of List
print("Average :", sum(numbers) / len(numbers))
print()

# Program 5 : Search an Element
key = 45
if key in numbers:
    print(key, "found in the list.")
else:
    print(key, "not found.")
print()

# Program 6 : Count Even and Odd Numbers
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Numbers :", even)
print("Odd Numbers  :", odd)
print()

# Program 7 : Remove Duplicates
duplicate_list = [10, 20, 10, 30, 20, 40, 50]
unique_list = list(set(duplicate_list))
print("Original :", duplicate_list)
print("Unique   :", unique_list)
print()

# Program 8 : Merge Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged List :", merged)
