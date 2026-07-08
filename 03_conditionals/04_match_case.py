"""
=========================================================
Topic       : Match Case Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
The match-case statement is used as an alternative to
multiple if-elif-else statements.

Available from Python 3.10 and above.

Syntax:

match variable:
    case value1:
        statement
    case value2:
        statement
    case _:
        default statement
"""

print("=" * 60)
print("MATCH CASE STATEMENT")
print("=" * 60)

# ----------------------------------------
# Example 1 : Week Days
# ----------------------------------------

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

print()

# ----------------------------------------
# Example 2 : Calculator
# ----------------------------------------

a = 20
b = 5
operator = "*"

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case "%":
        print(a % b)
    case _:
        print("Invalid Operator")

print()

# ----------------------------------------
# Example 3 : Traffic Signal
# ----------------------------------------

signal = "Red"

match signal:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid Signal")

print()

# ----------------------------------------
# Example 4 : Student Grade
# ----------------------------------------

grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Average")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

print()

# ----------------------------------------
# Example 5 : Fruit Name
# ----------------------------------------

fruit = "Mango"

match fruit:
    case "Apple":
        print("Red Fruit")
    case "Banana":
        print("Yellow Fruit")
    case "Mango":
        print("King of Fruits")
    case "Orange":
        print("Citrus Fruit")
    case _:
        print("Fruit Not Available")

print()

# ----------------------------------------
# Example 6 : Month Name
# ----------------------------------------

month = 8

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")

print()

print("=" * 60)
print("END OF MATCH CASE")
print("=" * 60)