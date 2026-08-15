"""
=========================================================
Topic       : Set Operations
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# Create Two Sets
# ----------------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1 :", set1)
print("Set 2 :", set2)

print()

# ----------------------------------------
# Union
# ----------------------------------------

print("Union :", set1 | set2)
print("Union using union() :", set1.union(set2))

print()

# ----------------------------------------
# Intersection
# ----------------------------------------

print("Intersection :", set1 & set2)
print("Intersection using intersection() :", set1.intersection(set2))

print()

# ----------------------------------------
# Difference
# ----------------------------------------

print("Set 1 - Set 2 :", set1 - set2)
print("Set 2 - Set 1 :", set2 - set1)

print()

# ----------------------------------------
# Difference using difference()
# ----------------------------------------

print("Difference :", set1.difference(set2))

print()

# ----------------------------------------
# Symmetric Difference
# ----------------------------------------

print("Symmetric Difference :", set1 ^ set2)
print(
    "Using symmetric_difference() :",
    set1.symmetric_difference(set2)
)

print()

# ----------------------------------------
# Subset
# ----------------------------------------

small_set = {1, 2, 3}
large_set = {1, 2, 3, 4, 5}

print("Is small_set a subset?", small_set.issubset(large_set))

print()

# ----------------------------------------
# Superset
# ----------------------------------------

print("Is large_set a superset?", large_set.issuperset(small_set))

print()

# ----------------------------------------
# Disjoint Sets
# ----------------------------------------

a = {1, 2, 3}
b = {4, 5, 6}

print("Are a and b disjoint?", a.isdisjoint(b))
