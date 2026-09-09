
# Day 06 — Data Visualization using Matplotlib and Seaborn

## Objective

The objective of Day 6 was to understand the importance of data visualization and learn how to represent data using meaningful charts.

For this task, I used the student dataset from Day 5 and created different visualizations using Matplotlib and Seaborn.

---

## What I Learned

### Data Visualization

Data visualization is the process of representing data using graphs and charts.

It helps us:

- Understand data more easily
- Identify patterns
- Compare values
- Understand distributions
- Identify trends
- Communicate results clearly

Data visualization is an important part of Data Science and Machine Learning because it helps us understand and analyze data before building Machine Learning models.

---

## Matplotlib

Matplotlib is a Python library used for creating graphs and visualizations.

I used Matplotlib to create:

- Bar Chart
- Line Chart
- Histogram
- Pie Chart

Example:

```python
import matplotlib.pyplot as plt

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()
````

---

## Seaborn

Seaborn is a Python data visualization library built on top of Matplotlib.

It provides a simple way to create statistical visualizations and works well with Pandas DataFrames.

I also practiced creating a bar chart using Seaborn.

Example:

```python
import seaborn as sns

sns.barplot(data=df, x="Name", y="Marks")
plt.show()
```

---

## Dataset Used

I reused the student dataset from Day 5.

The dataset contains:

* Student Name
* Age
* Marks
* City

The dataset also contains one missing value in the Marks column.

---

## Visualizations Created

### 1. Bar Chart

The Bar Chart was used to compare the marks of different students.

It makes it easy to identify which students have higher or lower marks.

```python
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
```

---

### 2. Line Chart

The Line Chart was used to visualize how student marks change from one student to another.

```python
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Marks Trend")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
```

---

### 3. Histogram

The Histogram was used to understand the distribution of student marks.

It groups marks into ranges and shows how many students fall into each range.

```python
plt.hist(df["Marks"].dropna(), bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
```

---

### 4. Pie Chart

The Pie Chart was used to show the distribution of students based on their cities.

```python
city_counts = df["City"].value_counts()

plt.pie(
    city_counts,
    labels=city_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Distribution by City")
plt.show()
```

---

## Observations

Based on the visualizations, I made the following observations:

1. Rahul has the highest marks in the dataset.

2. Vikram has the lowest marks in the dataset.

3. Most students have marks above 70.

4. The histogram shows that the marks are mostly concentrated in the higher range.

5. The pie chart shows that the students are distributed across Pune, Mumbai, and Nashik.

---

