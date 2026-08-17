"""
=========================================================
Topic       : Frozen Set
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Creating a Frozenset
# ----------------------------------------

numbers = frozenset([10, 20, 30, 40, 50])

print("Frozenset :", numbers)

print()

# ----------------------------------------
# Frozenset with Duplicate Values
# ----------------------------------------

data = frozenset([10, 20, 10, 30, 20, 40])

print("Frozenset with Duplicates :", data)

print()

# ----------------------------------------
# Type of Frozenset
# ----------------------------------------

print("Type :", type(numbers))

print()

# ----------------------------------------
# Length of Frozenset
# ----------------------------------------

print("Length :", len(numbers))

print()

# ----------------------------------------
# Frozenset is Immutable
# ----------------------------------------

# numbers.add(60)
# numbers.remove(10)

# The above operations are not allowed
# because frozensets are immutable.

# ----------------------------------------
# Set Operations with Frozenset
# ----------------------------------------

set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

print("Set 1 :", set1)
print("Set 2 :", set2)

print()

print("Union :", set1.union(set2))
print("Intersection :", set1.intersection(set2))
print("Difference :", set1.difference(set2))
print("Symmetric Difference :", set1.symmetric_difference(set2))

print()

# ----------------------------------------
# Membership Testing
# ----------------------------------------

if 20 in numbers:
    print("20 is present in the frozenset.")
else:
    print("20 is not present in the frozenset.")
