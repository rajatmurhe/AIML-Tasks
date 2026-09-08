# Day 5 - Pandas Practice
# Basic Dataset Analysis

import pandas as pd


# 1. Load CSV Dataset


df = pd.read_csv("dataset.csv")

print("===== Complete Dataset =====")
print(df)



# 2. Display First Five Rows


print("\n===== First Five Rows =====")
print(df.head())



# 3. Display Last Five Rows

print("\n===== Last Five Rows =====")
print(df.tail())



# 4. Check Number of Rows and Columns


print("\n===== Dataset Shape =====")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])



# 5. Display Column Names

print("\n===== Column Names =====")
print(df.columns.tolist())


# 6. Basic Dataset Information


print("\n===== Dataset Information =====")
df.info()


# 7. Find Missing Values

print("\n===== Missing Values =====")
print(df.isnull().sum())


# 8. Filter Students with Marks >= 80


print("\n===== Students with Marks >= 80 =====")

high_scorers = df[df["Marks"] >= 80]

print(high_scorers)



# 9. Filter Students Older Than 21


print("\n===== Students Older Than 21 =====")

older_students = df[df["Age"] > 21]

print(older_students)



# 10. Filter Students from Pune


print("\n===== Students from Pune =====")

pune_students = df[df["City"] == "Pune"]

print(pune_students)



# 11. Summary Statistics


print("\n===== Summary Statistics =====")

print(df.describe())



# 12. Average Marks


average_marks = df["Marks"].mean()

print("\nAverage Marks:", round(average_marks, 2))



# 13. Highest and Lowest Marks


highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)



# 14. Student with Highest Marks


print("\n===== Top Student =====")

highest_student = df.loc[df["Marks"].idxmax()]

print(highest_student)



# 15. Students with Missing Marks


print("\n===== Students with Missing Marks =====")

missing_marks = df[df["Marks"].isnull()]

print(missing_marks)



# 16. Final Analysis


print("\n===== Final Analysis =====")

print("Total Students:", len(df))
print("Total Columns:", len(df.columns))
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Missing Marks:", df["Marks"].isnull().sum())
