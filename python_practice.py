# Day 2 - Python Practice

# Variables
name = "Rajat"
age = 21
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# Data Types
number = 10
decimal = 10.5
text = "Python"
status = True
numbers = [10, 20, 30]
student = {"name": "Rajat", "age": 21}

print("\nData Types:")
print(type(number))
print(type(decimal))
print(type(text))
print(type(status))
print(type(numbers))
print(type(student))


# If-Else
marks = 85

if marks >= 90:
    print("\nGrade: A+")
elif marks >= 80:
    print("\nGrade: A")
elif marks >= 70:
    print("\nGrade: B")
elif marks >= 60:
    print("\nGrade: C")
else:
    print("\nGrade: F")


# For Loop
print("\nFor Loop:")
for i in range(1, 6):
    print(i)


# While Loop
print("\nWhile Loop:")
count = 1

while count <= 5:
    print(count)
    count += 1


# Function
def greet(name):
    return f"Hello, {name}!"


print("\nFunction:")
print(greet("Rajat"))
