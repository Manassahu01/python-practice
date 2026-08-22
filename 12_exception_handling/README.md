# ⚠️ Python Exception Handling

Welcome to the **Exception Handling** section of my **Python Practice** repository.

Exception handling is used to handle runtime errors in a controlled way so that a Python program does not stop unexpectedly.

This section covers the fundamentals of exception handling with simple, beginner-friendly, real-life examples.

---

## 📚 Topics Covered

- Exception Basics
- `try`
- `except`
- Multiple Exceptions
- `else`
- `finally`
- `raise`
- Built-in Exceptions
- Custom Exceptions
- Exception Handling Programs
- Practice Programs

---

## 📂 Folder Structure

```text
12_exception_handling/
│
├── README.md
├── 01_exception_basics.py
├── 02_try_except.py
├── 03_multiple_exceptions.py
├── 04_else_finally.py
├── 05_raise.py
├── 06_custom_exceptions.py
├── 07_exception_programs.py
└── 08_practice_programs.py
```

---

## 📖 What You Will Learn

After completing this section, you will be able to:

- Understand what an exception is.
- Identify common runtime errors.
- Handle errors using `try` and `except`.
- Handle different types of exceptions.
- Use `else` and `finally`.
- Manually raise an exception using `raise`.
- Create custom exceptions.
- Build programs that handle errors safely.

---

## 🔑 Basic Exception Handling

A simple exception-handling structure looks like this:

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")
```

Instead of allowing the program to crash, we can provide a useful message to the user.

---

## 🧩 Common Built-in Exceptions

| Exception | Meaning |
|---|---|
| `ValueError` | Invalid value |
| `TypeError` | Incorrect data type |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Invalid list/tuple index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File does not exist |
| `NameError` | Variable is not defined |

---

## 🔄 Exception Handling Flow

```text
try
 ↓
Code executes
 ↓
Error occurs?
 ├── No → else
 │
 └── Yes → except
             ↓
          finally
```

The `finally` block runs whether an exception occurs or not.

---

## 🏫 Real-Life Examples

Exception handling can be useful in situations such as:

- Taking valid user input.
- Handling incorrect calculations.
- Processing files safely.
- Validating student marks.
- Handling missing data.
- Building reliable applications.

---

## 🛠️ Requirements

- Python 3.x
- Visual Studio Code (or any Python IDE)

---

## 🚀 Getting Started

Navigate to the Exception Handling folder:

```bash
cd python-practice/12_exception_handling
```

Run the first program:

```bash
python 01_exception_basics.py
```

---

## 🎯 Learning Goal

The goal of this section is to learn how to identify, handle, and manage errors so that Python programs become more reliable and user-friendly.

---

## 📌 Note

The programs in this section are written in a simple and beginner-friendly way with practical examples.

---

Happy Coding! 🚀
