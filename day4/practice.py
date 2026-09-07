##Cell 1 — Import NumPy
import numpy as np

##Cell 2 — Creating a 1D Array

marks = np.array([70, 80, 90, 85, 75])

print("1D Array:")
print(marks)

print("Shape:", marks.shape)
print("Number of Dimensions:", marks.ndim)

##Cell 3 — Creating a 2D Array

marks_2d = np.array([
    [70, 80, 90],
    [85, 75, 95],
    [88, 92, 78]
])

print("2D Array:")
print(marks_2d)

print("Shape:", marks_2d.shape)
print("Number of Dimensions:", marks_2d.ndim)



##Cell 4 — Indexing

marks = np.array([70, 80, 90, 85, 75])

print("First element:", marks[0])
print("Third element:", marks[2])
print("Last element:", marks[-1])


##Cell 5 — 2D Indexing

marks_2d = np.array([
    [70, 80, 90],
    [85, 75, 95],
    [88, 92, 78]
])

print("First row, second column:", marks_2d[0, 1])
print("Second row, third column:", marks_2d[1, 2])


##Cell 6 — Slicing

marks = np.array([70, 80, 90, 85, 75])

print("First three marks:", marks[:3])
print("Marks from index 1 to 3:", marks[1:4])
print("Last two marks:", marks[-2:])


##Cell 7 — Mathematical Operations

marks = np.array([70, 80, 90, 85, 75])

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

##Cell 8 — Array Operations

marks = np.array([70, 80, 90, 85, 75])

print("Original Marks:", marks)

print("Marks + 5:", marks + 5)
print("Marks - 5:", marks - 5)
print("Marks * 2:", marks * 2)
print("Marks / 2:", marks / 2)

##Cell 9 — Python List vs NumPy Array

# Python List
python_marks = [70, 80, 90, 85, 75]

# NumPy Array
numpy_marks = np.array([70, 80, 90, 85, 75])

print("Python List:", python_marks)
print("NumPy Array:", numpy_marks)

print("\nNumPy Array + 5:")
print(numpy_marks + 5)

