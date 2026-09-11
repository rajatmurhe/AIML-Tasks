Great. Now paste this into `day8/README.md` on GitHub:

````markdown
# Day 8 — Data Cleaning and Preprocessing

## AI/ML Internship — Day 8

**Name:** Rajat Murhe  
**GitHub Repository:** [Linkific-Tasks](https://github.com/rajatmurhe/Linkific-Tasks)

---

## 1. Introduction

Day 8 focused on understanding why data preprocessing and cleaning are important before using data for analysis or Machine Learning.

For this task, I used the Netflix Movies and TV Shows dataset from the previous day's project and performed basic data cleaning and preprocessing using Pandas.

The objective was to identify missing values, handle them appropriately, remove duplicate records, rename columns where necessary, convert incorrect data types, and save the cleaned dataset.

---

## 2. Learning Objectives

The main objectives of this task were:

- Understand the importance of data preprocessing.
- Identify missing values in a dataset.
- Handle missing values using suitable techniques.
- Remove duplicate records.
- Rename columns where necessary.
- Convert incorrect data types.
- Save the cleaned dataset.
- Maintain the completed work on GitHub.

---

## 3. Dataset

The dataset used for this task is the Netflix Movies and TV Shows dataset.

The original dataset contains information about Netflix content including:

- Show ID
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

The original file used was:

```text
netflix_titles.csv
````

---

## 4. Technologies Used

* Python
* Pandas
* Google Colab
* Git
* GitHub

---

## 5. Data Loading

The dataset was loaded into a Pandas DataFrame using:

```python
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
```

After loading the dataset, I inspected the data to understand its structure and contents.

---

## 6. Missing Value Handling

I checked for missing values using:

```python
df.isnull().sum()
```

Several columns contained missing values.

For categorical columns such as `director`, `cast`, `country`, and `rating`, missing values were replaced with:

```text
Unknown
```

This allowed the records to be retained instead of unnecessarily deleting them.

---

## 7. Duplicate Record Removal

Duplicate records were identified using:

```python
df.duplicated().sum()
```

The duplicate records were then removed using:

```python
df = df.drop_duplicates()
```

This helped ensure that the cleaned dataset did not contain repeated records.

---

## 8. Column Renaming

The `show_id` column was renamed to `id`.

The `listed_in` column was renamed to `genres` to make the column name easier to understand.

```python
df = df.rename(columns={
    "show_id": "id",
    "listed_in": "genres"
})
```

---

## 9. Data Type Conversion

The `date_added` column was converted from text format into a proper datetime format.

```python
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)
```

This conversion makes the column easier to use for date-based analysis.

---

## 10. Final Dataset Validation

After cleaning, I checked the dataset again using:

```python
df.isnull().sum()
```

and:

```python
df.shape
```

I also verified the final data types and inspected the cleaned dataset.

The cleaned dataset was then saved as:

```text
netflix_titles_cleaned.csv
```

using:

```python
df.to_csv("netflix_titles_cleaned.csv", index=False)
```

---

## 11. Project Structure

```text
day8/
├── README.md
├── netflix_data_cleaning.ipynb
└── netflix_titles_cleaned.csv
```

### `netflix_data_cleaning.ipynb`

Contains the complete data cleaning and preprocessing workflow.

### `netflix_titles_cleaned.csv`

Contains the final cleaned version of the Netflix dataset.

### `README.md`

Contains the documentation and overview of the Day 8 task.

---

## 12. Data Cleaning Workflow

The complete workflow followed was:

```text
Load Dataset
      ↓
Explore Dataset
      ↓
Identify Missing Values
      ↓
Handle Missing Values
      ↓
Remove Duplicates
      ↓
Rename Columns
      ↓
Convert Data Types
      ↓
Validate Cleaned Dataset
      ↓
Save Cleaned Dataset
```

---

