"""
=========================================================
Topic       : Data Types in Python
Author      : Manas Sahu
Repository  : python-practice
Description : Learn Python built-in data types with
              simple examples.
=========================================================

Theory:
--------
Data types define the type of value stored in a variable.

Python has the following built-in data types:

1. int
2. float
3. complex
4. str
5. bool
6. list
7. tuple
8. set
9. dict
10. NoneType

You can check the type of any object using:
type(variable)
"""

print("=" * 60)
print("INTEGER (int)")
print("=" * 60)

age = 21
marks = 95
temperature = -10

print(age)
print(marks)
print(temperature)
print(type(age))

print("\n")

print("=" * 60)
print("FLOAT (float)")
print("=" * 60)

height = 5.8
price = 99.99
pi = 3.14159

print(height)
print(price)
print(pi)
print(type(price))

print("\n")

print("=" * 60)
print("COMPLEX (complex)")
print("=" * 60)

num1 = 4 + 5j
num2 = 10 - 2j

print(num1)
print(num2)
print(type(num1))

print("\n")

print("=" * 60)
print("STRING (str)")
print("=" * 60)

name = "Manas"
course = "Python"
city = 'Durg'

print(name)
print(course)
print(city)
print(type(name))

print("\n")

print("=" * 60)
print("BOOLEAN (bool)")
print("=" * 60)

is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
print(type(is_student))

print("\n")

print("=" * 60)
print("LIST")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(type(fruits))

print("\n")

print("=" * 60)
print("TUPLE")
print("=" * 60)

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))

print("\n")

print("=" * 60)
print("SET")
print("=" * 60)

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

print("\n")

print("=" * 60)
print("DICTIONARY")
print("=" * 60)

student = {
    "name": "Manas",
    "age": 21,
    "course": "BCA"
}

print(student)
print(type(student))

print("\n")

print("=" * 60)
print("NONETYPE")
print("=" * 60)

value = None

print(value)
print(type(value))

print("\n")

print("=" * 60)
print("CHECKING DATA TYPES")
print("=" * 60)

x = 100
y = 99.5
z = "Python"

print(type(x))
print(type(y))
print(type(z))

print("\n")

print("=" * 60)
print("TYPE CONVERSION")
print("=" * 60)

a = 10
b = float(a)

print(a)
print(type(a))

print(b)
print(type(b))

print("\n")

print("=" * 60)
print("MULTIPLE DATA TYPES")
print("=" * 60)

name = "Manas"
age = 21
cgpa = 8.5
passed = True

print(name, type(name))
print(age, type(age))
print(cgpa, type(cgpa))
print(passed, type(passed))

print("\n")

print("=" * 60)
print("PRACTICE QUESTIONS")
print("=" * 60)



print("\n")

print("=" * 60)
print("END OF DATA TYPES")
print("=" * 60)