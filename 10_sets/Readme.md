# 📖 Python Sets

Welcome to the **Sets** section of my **Python Practice** repository.

A set is a built-in Python data structure used to store multiple values in a single variable. Sets are **unordered, mutable, and do not allow duplicate values**.

This folder covers the fundamentals of Python sets with beginner-friendly examples and practice programs.

---

## 📚 Topics Covered

- Set Basics
- Set Methods
- Set Operations
- Set Traversal
- Frozen Sets
- Set Comprehension
- Set Programs
- Practice Programs

---

## 📂 Folder Structure

```text
10_sets/
│
├── README.md
├── 01_set_basics.py
├── 02_set_methods.py
├── 03_set_operations.py
├── 04_set_traversal.py
├── 05_frozen_set.py
├── 06_set_comprehension.py
├── 07_set_programs.py
└── 08_practice_programs.py
```

---

## 📖 What You Will Learn

After completing this section, you will be able to:

- Create sets.
- Add and remove elements from sets.
- Use common set methods.
- Perform mathematical set operations.
- Traverse sets using loops.
- Understand `frozenset`.
- Use set comprehensions.
- Remove duplicate values from data.
- Solve set-based programming problems.

---

## 🔑 Important Characteristics of Sets

### 1. Unordered

Sets do not maintain a fixed order of elements.

```python
numbers = {10, 20, 30, 40}
```

The order in which elements are displayed may not be the same as the order in which they were added.

---

### 2. No Duplicate Values

Sets automatically remove duplicate values.

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

---

### 3. Mutable

Elements can be added or removed from a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

### 4. No Indexing

Sets do not support indexing because they are unordered.

```python
numbers = {10, 20, 30}

# This will give an error:
# print(numbers[0])
```

---

## 🆚 List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---|---|---|---|
| Syntax | `[]` | `()` | `{}` |
| Ordered | Yes | Yes | No |
| Mutable | Yes | No | Yes |
| Duplicates | Yes | Yes | No |
| Indexing | Yes | Yes | No |
| Slicing | Yes | Yes | No |
| Use Case | General collection | Fixed data | Unique data |

---

## 🛠️ Requirements

- Python 3.x
- Visual Studio Code (or any Python IDE)

---

## 🚀 Getting Started

Navigate to the Sets folder:

```bash
cd python-practice/10_sets
```

Run the first program:

```bash
python 01_set_basics.py
```

---

## 🎯 Learning Goal

The goal of this section is to build a strong understanding of Python sets and learn how they can be used to work with unique values and perform mathematical set operations.

---

## 📌 Note

All examples are written in a simple and beginner-friendly way to strengthen Python fundamentals.

---

Happy Coding! 🚀
