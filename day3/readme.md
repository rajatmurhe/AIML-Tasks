# Day 03 — Python Data Structures and File Handling

## Objective

The objective of Day 3 was to learn Python data structures and understand how to store, organize, retrieve, and manage simple data using Python.

The main topics covered were Lists, Tuples, Dictionaries, Sets, File Handling, and Python Modules.

---

## What I Learned

### Lists

Lists are ordered and changeable collections used to store multiple values.

```python
students = ["Rajat", "Amit", "Rahul"]
```
I learned how to create lists, access elements, add elements, remove elements, and iterate through lists.

Tuples

Tuples are ordered collections that cannot be changed after creation.

student = ("Rajat", 21, "A")

I learned how tuples can be used when data should remain unchanged.

Dictionaries

Dictionaries store data in key-value pairs.

student = {
    "name": "Rajat",
    "age": 21,
    "grade": "A"
}

I learned how to create dictionaries, access values using keys, add new key-value pairs, and update existing data.

Sets

Sets are collections that store unique values.

numbers = {1, 2, 3, 3, 4}

Duplicate values are automatically removed from a set.

I learned that sets are useful when working with unique data.

File Handling

I learned how Python can be used to read and write data to files.

The main operations I practiced were:

Opening files
Reading files
Writing to files
Appending data
Working with files using with open()

Example:

with open("students.txt", "w") as file:
    file.write("Rajat, 21, A\n")

File handling allows data to be stored permanently instead of being available only while the program is running.

Projects
1. Python Data Structures Practice

I created a Python practice file covering Lists, Tuples, Dictionaries, Sets, and basic File Handling.

File:

python_data_structures.py

The program demonstrates how different Python data structures work and how files can be created, written to, read, and updated.

2. Student Record Management System

I built a Student Record Management System using Python.

The system allows the user to:

Add student records
View student records
Search for a student
Store student records in a text file
Retrieve records from the text file

The project combines Python data structures, functions, conditional statements, loops, and file handling.

Student Record Management System

The system provides a simple menu:

================================
 Student Record Management
================================
1. Add Student
2. View Students
3. Search Student
4. Exit

Student records are stored in:

students.txt

Example record:

101,Rajat,21,A
102,Amit,22,B
103,Rahul,21,A+

The program can read these records from the file and display or search them when required.

Project Structure
Day-03/
│
├── README.md
├── python_data_structures.py
├── student_record_management.py
├── students.txt
└── practice.txt
python_data_structures.py

Contains practice programs for Lists, Tuples, Dictionaries, Sets, and File Handling.

student_record_management.py

Contains the Student Record Management System.

students.txt

Stores student records used by the Student Record Management System.

practice.txt

Used for practicing basic Python file reading, writing, and appending operations.
