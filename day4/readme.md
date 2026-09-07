
# Day 04 — NumPy and Numerical Computing

## Objective

The objective of Day 4 was to understand NumPy and its importance in Artificial Intelligence and Machine Learning.

I learned how to create and work with NumPy arrays, perform indexing and slicing, apply mathematical operations, and understand the difference between Python Lists and NumPy Arrays.

To apply these concepts practically, I created a Student Marks Analysis project using NumPy.

---

## What I Learned

### NumPy

NumPy stands for Numerical Python. It is a Python library used for numerical computing and working with arrays.

NumPy is widely used in:

- Data Analysis
- Machine Learning
- Deep Learning
- Scientific Computing
- Numerical Computing

It provides efficient operations for working with numerical data and forms an important foundation for many AI/ML libraries.

---

## NumPy Arrays

I learned how to create NumPy arrays using `np.array()`.

### 1D Array

A one-dimensional array stores values in a single sequence.

```python
import numpy as np

marks = np.array([70, 80, 90, 85, 75])

print(marks)
````

### 2D Array

A two-dimensional array stores data in rows and columns.

```python
marks = np.array([
    [70, 80, 90],
    [85, 75, 95],
    [88, 92, 78]
])

print(marks)
```

2D arrays are useful for representing structured numerical datasets.

---

## Indexing and Slicing

I learned how to access individual elements of an array using indexing.

```python
marks = np.array([70, 80, 90, 85, 75])

print(marks[0])
print(marks[2])
```

I also practiced slicing:

```python
print(marks[1:4])
```

For 2D arrays, I learned how to access values using row and column positions.

```python
print(marks[0, 1])
```

---

## Mathematical Operations

I practiced common mathematical operations using NumPy.

```python
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
```

These operations can be used to quickly analyze numerical data.

---

## Python Lists vs NumPy Arrays

I compared Python Lists with NumPy Arrays.

### Python List

```python
marks = [70, 80, 90, 85, 75]
```

Python Lists are general-purpose collections that can store different types of values.

### NumPy Array

```python
marks = np.array([70, 80, 90, 85, 75])
```

NumPy Arrays are specifically designed for numerical operations and provide efficient array-based calculations.

For example:

```python
marks + 5
```

adds 5 to every element of a NumPy array.

This makes NumPy useful when working with numerical datasets in Machine Learning and Data Science.

---

# Projects

## 1. NumPy Practice Notebook

I created a Jupyter Notebook to practice the fundamental concepts of NumPy.

The notebook covers:

* NumPy installation
* 1D arrays
* 2D arrays
* Array shape and dimensions
* Indexing
* Slicing
* Mathematical operations
* Array arithmetic
* Python Lists vs NumPy Arrays

File:

```text
numpy_practice.ipynb
```

---

## 2. Student Marks Analysis

I created a Student Marks Analysis project using NumPy.

The project stores student names and marks in NumPy arrays and calculates useful statistics.

The analysis includes:

* Total marks
* Average marks
* Highest marks
* Lowest marks
* Highest scoring student
* Lowest scoring student

Example:

```text
Student Marks:
Rajat : 78
Amit : 85
Rahul : 92
Priya : 67
Sneha : 88

Total Marks: 410
Average Marks: 82.0
Highest Marks: 92
Highest Scoring Student: Rahul
Lowest Marks: 67
Lowest Scoring Student: Priya
```

This project helped me apply NumPy concepts to a simple real-world data analysis problem.

---

## Project Structure

```text
Day-04/
│
├── README.md
├── numpy_practice.ipynb
└── student_marks_analysis.py
```

### `numpy_practice.ipynb`

Contains practical examples and exercises covering NumPy arrays, indexing, slicing, mathematical operations, and comparison with Python Lists.

### `student_marks_analysis.py`

Contains the Student Marks Analysis project implemented using NumPy.

---

## GitHub Update

I organized my Day 4 work into a separate `Day-04` folder and uploaded the completed work to my GitHub repository.

Repository:

**Linkific-Tasks**

[https://github.com/rajatmurhe/Linkific-Tasks](https://github.com/rajatmurhe/Linkific-Tasks)

I used Git to track the changes, create a commit, and push the completed Day 4 work to GitHub.

---
