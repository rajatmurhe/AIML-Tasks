pip install pandas matplotlib seaborn

import pandas as pd

# Creating sample data to fix the FileNotFoundError
data = {
    'Name': ['Rahul', 'Vikram', 'Sneha', 'Anita', 'John'],
    'Marks': [95, 45, 88, 72, 80],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}

df_sample = pd.DataFrame(data)
df_sample.to_csv('dataset.csv', index=False)
print("File 'dataset.csv' has been created successfully.")


# Day 6 - Data Visualization
# Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load Dataset


df = pd.read_csv("dataset.csv")

print("===== Dataset =====")
print(df)


# 2. Basic Dataset Information

print("\n===== Dataset Information =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== Missing Values =====")
print(df.isnull().sum())



# 3. Bar Chart - Student Marks


plt.figure(figsize=(10, 6))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 4. Line Chart - Student Marks


plt.figure(figsize=(10, 6))

plt.plot(df["Name"], df["Marks"], marker="o")

plt.title("Student Marks Trend")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 5. Histogram - Marks Distribution


plt.figure(figsize=(8, 6))

plt.hist(df["Marks"].dropna(), bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()


# 6. Pie Chart - Students by City


city_counts = df["City"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    city_counts,
    labels=city_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Distribution by City")

plt.show()


# 7. Seaborn Visualization


plt.figure(figsize=(10, 6))

sns.barplot(
    data=df,
    x="Name",
    y="Marks"
)

plt.title("Student Marks using Seaborn")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 8. Observations


print("\n===== Observations =====")

print("1. Rahul has the highest marks in the dataset.")
print("2. Vikram has the lowest marks in the dataset.")
print("3. Most students have marks above 70.")
print("4. The histogram shows that most marks are concentrated in the higher range.")
print("5. The pie chart shows the distribution of students across different cities.")
