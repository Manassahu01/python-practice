"""
=========================================================
Topic       : Set Methods
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create a Set
# ----------------------------------------

numbers = {10, 20, 30, 40}

print("Original Set :", numbers)

print()

# ----------------------------------------
# add()
# ----------------------------------------

numbers.add(50)

print("After add() :", numbers)

print()

# ----------------------------------------
# update()
# ----------------------------------------

numbers.update([60, 70, 80])

print("After update() :", numbers)

print()

# ----------------------------------------
# remove()
# ----------------------------------------

numbers.remove(20)

print("After remove() :", numbers)

print()

# ----------------------------------------
# discard()
# ----------------------------------------

numbers.discard(30)

print("After discard() :", numbers)

# discard() does not give an error
# if the element does not exist.

numbers.discard(100)

print("After discarding 100 :", numbers)

print()

# ----------------------------------------
# pop()
# ----------------------------------------

removed = numbers.pop()

print("Removed Element :", removed)
print("After pop() :", numbers)

print()

# ----------------------------------------
# copy()
# ----------------------------------------

copy_set = numbers.copy()

print("Copied Set :", copy_set)

print()

# ----------------------------------------
# clear()
# ----------------------------------------

temp = {1, 2, 3}

print("Before clear() :", temp)

temp.clear()

print("After clear() :", temp)

print()

# ----------------------------------------
# remove() vs discard()
# ----------------------------------------

example = {10, 20, 30}

# remove() gives KeyError if the
# element does not exist.
# example.remove(100)

# discard() does not give an error.
example.discard(100)

print("Final Set :", example)
