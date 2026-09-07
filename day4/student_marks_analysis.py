import numpy as np

print("===== Student Marks Analysis =====")

# Student names
students = np.array(["Rajat", "Amit", "Rahul", "Priya", "Sneha"])

# Student marks
marks = np.array([78, 85, 92, 67, 88])

print("\nStudent Marks:")
for i in range(len(students)):
    print(students[i], ":", marks[i])

# Calculations
total_marks = np.sum(marks)
average_marks = np.mean(marks)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)

# Find highest and lowest scoring students
highest_index = np.argmax(marks)
lowest_index = np.argmin(marks)

highest_student = students[highest_index]
lowest_student = students[lowest_index]

# Display results
print("\n===== Analysis =====")

print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks, 2))
print("Highest Marks:", highest_marks)
print("Highest Scoring Student:", highest_student)
print("Lowest Marks:", lowest_marks)
print("Lowest Scoring Student:", lowest_student)