# Day 3 - Python Data Structures Practice


# 1. Lists


students = ["Rajat", "Amit", "Rahul"]

print("Students List:")
print(students)

# Add a student
students.append("Priya")

print("After adding a student:")
print(students)

# Access an element
print("First student:", students[0])



# 2. Tuples


student_details = ("Rajat", 21, "A")

print("\nStudent Tuple:")
print(student_details)

print("Student Name:", student_details[0])
print("Student Age:", student_details[1])
print("Student Grade:", student_details[2])



# 3. Dictionaries


student = {
    "name": "Rajat",
    "age": 21,
    "grade": "A"
}

print("\nStudent Dictionary:")
print(student)

print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])

# Add new key-value pair
student["course"] = "AI/ML"

print("Updated Dictionary:")
print(student)



# 4. Sets


numbers = {1, 2, 3, 3, 4, 5}

print("\nSet:")
print(numbers)

# Add a value
numbers.add(6)

print("Updated Set:")
print(numbers)



# 5. File Handling


file_name = "practice.txt"

# Writing to a file
with open(file_name, "w") as file:
    file.write("Python Data Structures Practice\n")
    file.write("Learning Lists, Tuples, Dictionaries and Sets.\n")

# Reading from a file
print("\nFile Content:")

with open(file_name, "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open(file_name, "a") as file:
    file.write("Practicing File Handling in Python.\n")

print("File updated successfully.")
