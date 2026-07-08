"""
=========================================================
Topic       : Nested If Statement
Author      : Manas Sahu
Repository  : python-practice
=========================================================

Theory:
--------
A Nested If means writing one if statement inside another
if statement.

It is used when multiple conditions depend on each other.

Syntax:

if condition1:
    if condition2:
        statement
"""

print("=" * 60)
print("NESTED IF STATEMENT")
print("=" * 60)

# ----------------------------------------
# Example 1 : Voting Eligibility
# ----------------------------------------

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible for Voting")
    else:
        print("Not an Indian Citizen")
else:
    print("Not Eligible for Voting")

print()

# ----------------------------------------
# Example 2 : Student Result
# ----------------------------------------

marks = 85
attendance = 80

if marks >= 33:
    if attendance >= 75:
        print("Student Passed")
    else:
        print("Attendance is Low")
else:
    print("Student Failed")

print()

# ----------------------------------------
# Example 3 : ATM Withdrawal
# ----------------------------------------

balance = 10000
pin = 1234
entered_pin = 1234
amount = 5000

if entered_pin == pin:
    if amount <= balance:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")

print()

# ----------------------------------------
# Example 4 : Login System
# ----------------------------------------

username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

print()

# ----------------------------------------
# Example 5 : College Admission
# ----------------------------------------

percentage = 82
documents_verified = True

if percentage >= 60:
    if documents_verified:
        print("Admission Confirmed")
    else:
        print("Verify Your Documents")
else:
    print("Admission Rejected")

print()

# ----------------------------------------
# Example 6 : Online Shopping
# ----------------------------------------

cart_amount = 2500
premium_member = True

if cart_amount >= 1000:
    if premium_member:
        print("Free Delivery")
    else:
        print("Delivery Charges Applicable")
else:
    print("Minimum Order Not Reached")

print()

# ----------------------------------------
# Example 7 : Employee Bonus
# ----------------------------------------

experience = 5
performance = "Excellent"

if experience >= 3:
    if performance == "Excellent":
        print("Bonus Approved")
    else:
        print("No Bonus")
else:
    print("Experience Not Sufficient")

print()

# ----------------------------------------
# Example 8 : Exam Eligibility
# ----------------------------------------

attendance = 90
fees_paid = True

if attendance >= 75:
    if fees_paid:
        print("Eligible for Exam")
    else:
        print("Pay Pending Fees")
else:
    print("Attendance Shortage")

print()

print("=" * 60)
print("END OF NESTED IF")
print("=" * 60)