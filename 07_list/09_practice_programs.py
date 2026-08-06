"""
=========================================================
Topic       : List Practice Programs
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Program 1 : Reverse a List
# ----------------------------------------

numbers = [10, 20, 30, 40, 50]
print("Original :", numbers)
print("Reversed :", numbers[::-1])

print()

# ----------------------------------------
# Program 2 : Find Second Largest Element
# ----------------------------------------

nums = [12, 45, 7, 89, 34]
temp = sorted(nums)
print("Second Largest :", temp[-2])

print()

# ----------------------------------------
# Program 3 : Count Occurrences
# ----------------------------------------

items = [10, 20, 10, 30, 10, 40]
print("Count of 10 :", items.count(10))

print()

# ----------------------------------------
# Program 4 : Remove an Element
# ----------------------------------------

fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.remove("Banana")
print(fruits)

print()

# ----------------------------------------
# Program 5 : Insert an Element
# ----------------------------------------

fruits.insert(1, "Kiwi")
print(fruits)

print()

# ----------------------------------------
# Program 6 : Check if List is Empty
# ----------------------------------------

data = []

if len(data) == 0:
    print("List is Empty")
else:
    print("List is Not Empty")

print()

# ----------------------------------------
# Program 7 : Copy a List
# ----------------------------------------

copy_list = nums.copy()
print(copy_list)

print()

# ----------------------------------------
# Program 8 : Find Common Elements
# ----------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common Elements :", common)

print()

# ----------------------------------------
# Program 9 : Remove Duplicate Elements
# ----------------------------------------

duplicate = [1, 2, 2, 3, 4, 4, 5]
print(list(set(duplicate)))

print()

# ----------------------------------------
# Program 10 : Sort List in Descending Order
# ----------------------------------------

marks = [78, 45, 92, 66, 81]
marks.sort(reverse=True)
print(marks)
