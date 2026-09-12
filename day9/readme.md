
# Day 9 — Exploratory Data Analysis

## AI/ML Internship — Day 9

**Name:** Rajat Murhe  
**GitHub Repository:** [Linkific-Tasks](https://github.com/rajatmurhe/Linkific-Tasks)

---

## 1. Introduction

Day 9 focused on **Exploratory Data Analysis (EDA)** and understanding how to explore a dataset before using it for further analysis or Machine Learning.

For this task, I used the cleaned Netflix Movies and TV Shows dataset from Day 8.

The goal was to perform descriptive statistics, identify patterns and trends, create meaningful visualizations, and extract useful business insights from the dataset.

---

## 2. Learning Objectives

The main objectives of this task were:

- Understand the purpose of Exploratory Data Analysis.
- Explore a cleaned dataset before further analysis.
- Perform descriptive statistics.
- Identify trends and patterns.
- Create meaningful data visualizations.
- Extract business insights from the dataset.
- Update the completed work on GitHub.

---

## 3. Dataset

The dataset used for this task is the cleaned Netflix Movies and TV Shows dataset created during Day 8.

It contains information such as:

- ID
- Type
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genres
- Description

The cleaned dataset contains **8,807 titles and 12 columns**.

---

## 4. Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Google Colab
- Git
- GitHub

---

## 5. Loading the Dataset

I loaded the cleaned Netflix dataset into a Pandas DataFrame using:

```python
import pandas as pd

df = pd.read_csv("netflix_titles_cleaned.csv")
````

After loading the dataset, I displayed the first few records and checked the size and structure of the data.

---

## 6. Descriptive Statistics

I used Pandas functions such as:

```python
df.shape
df.info()
df.describe(include="all")
```

These functions helped me understand:

* Number of rows and columns
* Data types
* Basic statistical information
* Overall structure of the dataset

Descriptive statistics provided an initial understanding of the dataset before performing deeper analysis.

---

## 7. Movies vs TV Shows Analysis

I analyzed the distribution of Movies and TV Shows.

The dataset contains:

* **6,131 Movies**
* **2,676 TV Shows**

This shows that Movies make up the larger portion of the Netflix dataset.

A visualization was created to clearly compare the two content types.

---

## 8. Release Year Analysis

I analyzed the number of Netflix titles across different release years.

The top release years were:

* **2018 — 1,147 titles**
* **2017 — 1,032 titles**
* **2019 — 1,030 titles**
* **2020 — 953 titles**
* **2016 — 902 titles**

Among these, **2018 had the highest number of titles**.

A line chart was used to understand the distribution of titles across different release years.

---

## 9. Country Analysis

I analyzed the countries associated with Netflix titles.

Since some records contain multiple countries, the country values were separated before counting them.

The top countries were:

* **United States — 3,689**
* **India — 1,046**
* **Unknown — 831**
* **United Kingdom — 804**
* **Canada — 445**

The United States has the highest representation in the dataset.

---

## 10. Genre Analysis

I analyzed the `genres` column to identify the most common genres.

Since a single title can belong to multiple genres, the genre values were separated before counting them.

The top genres were:

* **International Movies — 2,752**
* **Dramas — 2,427**
* **Comedies — 1,674**
* **International TV Shows — 1,351**
* **Documentaries — 869**

International Movies was the most common genre in the dataset.

---

## 11. Content Rating Analysis

I also analyzed the content ratings to understand the distribution of different ratings.

The top ratings were:

* **TV-MA — 3,207**
* **TV-14 — 2,160**
* **TV-PG — 863**
* **R — 799**
* **PG-13 — 490**

TV-MA was the most common rating in the dataset.

---

## 12. Data Visualizations

Three main visualizations were created as part of this task.

### 1. Movies vs TV Shows

A chart was used to compare the number of Movies and TV Shows.

### 2. Netflix Content by Release Year

A line chart was used to show how titles are distributed across release years.

### 3. Top Countries

A chart was used to compare the countries with the highest number of Netflix titles.

These visualizations helped make the dataset easier to understand and helped identify patterns more clearly.

---

## 13. Business Insights

Based on the EDA, I identified the following business insights:

1. **Movies dominate the Netflix dataset**, with 6,131 Movies compared with 2,676 TV Shows.

2. **The United States has the highest representation**, with 3,689 titles, followed by India with 1,046 titles.

3. **International Movies is the most common genre**, with 2,752 titles, followed by Dramas and Comedies.

4. **TV-MA is the most common content rating**, with 3,207 titles, followed by TV-14 with 2,160 titles.

5. **2018 had the highest number of titles by release year**, with 1,147 titles.

---

## 14. EDA Workflow

The complete workflow followed during this task was:

```text
Load Cleaned Dataset
        ↓
Explore Dataset
        ↓
Perform Descriptive Statistics
        ↓
Analyze Content Types
        ↓
Analyze Release Years
        ↓
Analyze Countries
        ↓
Analyze Genres
        ↓
Analyze Ratings
        ↓
Create Visualizations
        ↓
Extract Business Insights
```

---

## 15. Project Structure

```text
day9/
├── README.md
└── netflix_eda.ipynb
```

### `netflix_eda.ipynb`

Contains the complete EDA process, including dataset exploration, descriptive statistics, analysis, visualizations, and business insights.

---

## 16. Key Takeaways

Through this task, I learned how Exploratory Data Analysis can be used to understand a dataset before building Machine Learning models.

I learned how to use Pandas for descriptive analysis and how to identify patterns by comparing different columns.

I also learned that visualizations make large datasets easier to understand and help communicate findings clearly.

Most importantly, I learned how to convert analysis results into practical business insights.

---

## 17. Challenges Faced

* Understanding which parts of the dataset were most useful for analysis.
* Working with columns containing multiple countries or genres in a single record.
* Choosing meaningful visualizations for the available time.
* Converting numerical analysis results into simple business insights.
* Making sure the insights were based on the actual dataset results.

---
