# Student Grade Calculator

print("===== Student Grade Calculator =====")

name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Student Result =====")
print("Student:", name)
print("Marks:", marks)

if 0 <= marks <= 100:
    print("Grade:", grade)
