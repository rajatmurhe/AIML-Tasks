# Day 05 — Pandas and Basic Dataset Analysis

## Objective

The objective of Day 5 was to learn Pandas and understand how it can be used to work with structured datasets.

The main tasks were to load a CSV dataset, understand DataFrames, inspect the data, identify missing values, filter records using conditions, and generate summary statistics.

---

## What I Learned

### Pandas

Pandas is a Python library used for data manipulation and data analysis.

It is commonly used for:

- Loading datasets
- Exploring data
- Cleaning data
- Filtering records
- Handling missing values
- Preparing data for Machine Learning

### DataFrame

A DataFrame is a two-dimensional table-like data structure containing rows and columns.

It is similar to a spreadsheet and is useful for working with structured datasets.

---

## Dataset

For this practice, I used a student dataset containing:

- Name
- Age
- Marks
- City

The dataset also contains a missing marks value so that missing-value detection can be practiced.

---

## Operations Performed

### Load CSV

```python
df = pd.read_csv("dataset.csv")
