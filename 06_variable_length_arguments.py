"""
=========================================================
Topic       : Variable Length Arguments
Author      : Manas Sahu
Repository  : python-practice
=========================================================
"""

# ----------------------------------------
# *args Example
# ----------------------------------------

def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    print("Sum :", total)


add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)

print()

# ----------------------------------------
# Find Maximum Using *args
# ----------------------------------------

def maximum(*numbers):
    print("Maximum Value :", max(numbers))


maximum(10, 50, 30, 90, 25)

print()

# ----------------------------------------
# **kwargs Example
# ----------------------------------------

def student(**details):

    for key, value in details.items():
        print(key, ":", value)


student(name="Manas", age=20, course="BCA")

print()

# ----------------------------------------
# *args and **kwargs Together
# ----------------------------------------

def demo(*args, **kwargs):

    print("Args :", args)
    print("Kwargs :", kwargs)


demo(10, 20, 30, name="Manas", city="Bhopal")
