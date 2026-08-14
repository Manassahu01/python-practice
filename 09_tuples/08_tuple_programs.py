"""
=========================================================
Topic       : Tuple Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# Program 1 : Find Largest Element
numbers = (12, 45, 7, 89, 34)
print("Largest Element :", max(numbers))
print()

# Program 2 : Find Smallest Element
print("Smallest Element :", min(numbers))
print()

# Program 3 : Find Sum of Elements
print("Sum :", sum(numbers))
print()

# Program 4 : Find Average
average = sum(numbers) / len(numbers)
print("Average :", average)
print()

# Program 5 : Search an Element
key = 45
if key in numbers:
    print(key, "found in the tuple.")
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

# Program 7 : Reverse a Tuple
print("Reversed Tuple :", numbers[::-1])
print()

# Program 8 : Sort a Tuple
sorted_tuple = tuple(sorted(numbers))
print("Sorted Tuple :", sorted_tuple)
print()

# Program 9 : Remove Duplicates
duplicate = (10, 20, 10, 30, 20, 40)
unique_tuple = tuple(set(duplicate))

print("Original Tuple :", duplicate)
print("Unique Tuple   :", unique_tuple)
print()

# Program 10 : Concatenate Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print("Combined Tuple :", combined)
