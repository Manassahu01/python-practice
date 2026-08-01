"""
=========================================================
Topic       : List Methods
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a List
# ----------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("Original List :", fruits)

print()

# append()
fruits.append("Orange")
print("append() :", fruits)

print()

# extend()
fruits.extend(["Kiwi", "Grapes"])
print("extend() :", fruits)

print()

# insert()
fruits.insert(1, "Pineapple")
print("insert() :", fruits)

print()

# remove()
fruits.remove("Banana")
print("remove() :", fruits)

print()

# pop()
item = fruits.pop()
print("Removed Item :", item)
print("pop() :", fruits)

print()

# index()
print("Index of Mango :", fruits.index("Mango"))

print()

# count()
numbers = [10, 20, 10, 30, 10, 40]
print("Count of 10 :", numbers.count(10))

print()

# sort()
marks = [78, 45, 92, 66, 81]
marks.sort()
print("Ascending :", marks)

marks.sort(reverse=True)
print("Descending :", marks)

print()

# reverse()
marks.reverse()
print("reverse() :", marks)

print()

# copy()
copy_list = marks.copy()
print("Copied List :", copy_list)

print()

# clear()
temp = ["A", "B", "C"]
temp.clear()
print("clear() :", temp)
