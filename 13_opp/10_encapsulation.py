"""
10. Encapsulation in Python
---------------------------

Encapsulation keeps data and the methods that work with it together inside
a class. It can also control how data is accessed or updated.

Python uses naming conventions rather than strict access modifiers:
- public_name: accessible normally
- _protected_name: convention for internal use; not enforced by Python
- __private_name: name-mangled to reduce accidental access
"""


# 1. Public attributes
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


student = Student("Aarav", 85)
student.show_details()
print("Public name:", student.name)
print()


# 2. Protected-style attributes: single underscore
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Convention: intended for internal use

    def show_salary(self):
        print(f"{self.name}'s salary: ₹{self._salary}")


employee = Employee("Priya", 35000)
employee.show_salary()
# Direct access still works, but code outside the class should respect
# the single-underscore convention.
print("Direct _salary access is possible:", employee._salary)
print()


# 3. Name-mangled attributes: double underscore
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print(f"{self.owner}'s balance: ₹{self.__balance}")


account = BankAccount("Riya", 5000)
account.show_balance()
# print(account.__balance)  # Uncomment to see the AttributeError.
print()


# 4. Getter and setter methods with validation
class StudentRecord:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.set_marks(marks)

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks. Enter a value from 0 to 100.")

    def show_record(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.__marks}")


record = StudentRecord("Kabir", 78)
record.show_record()
print("Marks using getter:", record.get_marks())
record.set_marks(92)
print("Updated marks:", record.get_marks())
record.set_marks(150)  # Rejected by validation
print("Marks after invalid update:", record.get_marks())
print()


# 5. Bank account with validated deposits and withdrawals
class SafeBankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance


safe_account = SafeBankAccount("Aman", 2000)
safe_account.deposit(500)
safe_account.withdraw(300)
safe_account.withdraw(5000)
safe_account.deposit(-100)
print("Final balance:", safe_account.get_balance())
print()


# 6. Encapsulation using a property
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Calls the property setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product("Keyboard", 1200)
print(f"{product.name} price: ₹{product.price}")
product.price = 1500
print(f"Updated price: ₹{product.price}")
# product.price = -50  # Uncomment to test validation.
print()


# 7. Quick summary
print("Encapsulation summary:")
print("- Public: name")
print("- Single underscore: _salary (convention, not enforced)")
print("- Double underscore: __balance (name mangling)")
print("- Getters, setters, and properties can validate updates")
