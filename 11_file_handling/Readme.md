# 📖 Python File Handling

Welcome to the **File Handling** section of my **Python Practice** repository.

File handling allows us to create, read, write, update, and manage files using Python. It is an important concept because real-world applications often need to store and retrieve data from files.

This folder covers the fundamentals of Python file handling with beginner-friendly examples and practice programs.

---

## 📚 Topics Covered

- File Handling Basics
- Opening Files
- Reading Files
- Writing Files
- Appending Data
- File Modes
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `writelines()`
- `with open()`
- Closing Files
- File Handling Programs
- Practice Programs

---

## 📂 Folder Structure

```text
11_file_handling/
│
├── README.md
├── 01_file_basics.py
├── 02_reading_files.py
├── 03_writing_files.py
├── 04_appending_files.py
├── 05_file_modes.py
├── 06_with_statement.py
├── 07_file_programs.py
└── 08_practice_programs.py
```

---

## 📖 What You Will Learn

After completing this section, you will be able to:

- Open files using Python.
- Read data from files.
- Write data into files.
- Append new data to existing files.
- Understand different file modes.
- Use `read()`, `readline()`, and `readlines()`.
- Use `write()` and `writelines()`.
- Close files properly.
- Use the `with open()` statement.
- Solve file-handling programming problems.

---

## 🔑 Common File Modes

| Mode | Description |
|---|---|
| `r` | Read the file |
| `w` | Write to the file |
| `a` | Append data to the file |
| `r+` | Read and write |
| `w+` | Write and read |
| `a+` | Append and read |

---

## 📝 Basic File Syntax

### Opening a File

```python
file = open("data.txt", "r")
```

### Reading a File

```python
file = open("data.txt", "r")

data = file.read()

print(data)

file.close()
```

### Writing to a File

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

---

## ⭐ Using `with open()`

The `with` statement automatically handles closing the file.

```python
with open("data.txt", "r") as file:
    data = file.read()
    print(data)
```

This is the recommended way to work with files in Python.

---

## 🛠️ Requirements

- Python 3.x
- Visual Studio Code (or any Python IDE)

---

## 🚀 Getting Started

Navigate to the File Handling folder:

```bash
cd python-practice/11_file_handling
```

Run the first program:

```bash
python 01_file_basics.py
```

---

## 🎯 Learning Goal

The goal of this section is to understand how Python interacts with files and how file handling can be used to store, retrieve, and manage data.

---

## 📌 Note

The programs in this section are written in a simple and beginner-friendly way to strengthen Python fundamentals.

---

Happy Coding! 🚀
