
# Day 11 — Classification with Machine Learning

## Introduction

On Day 11 of my AI/ML internship, I learned the basics of **classification problems** in Machine Learning.

Classification is used when the output belongs to a specific category or class. In this task, I created a simple student dataset and classified students into **Pass** and **Fail** categories.

I trained and compared two classification algorithms:

- Logistic Regression
- Decision Tree Classifier

## Objectives

- Understand classification problems.
- Convert numerical data into classification labels.
- Train a Logistic Regression model.
- Train a Decision Tree model.
- Evaluate both models using accuracy.
- Compare the model results.
- Make predictions on new data.

## Dataset

The dataset contains:

- `Hours_Studied` — Number of hours a student studied.
- `Marks` — Marks obtained by the student.
- `Result` — Classification label.

The classification rule used was:

- `1` → Pass (Marks >= 50)
- `0` → Fail (Marks < 50)

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Google Colab
- GitHub

## Machine Learning Models

### Logistic Regression

Logistic Regression was used as a binary classification algorithm to predict whether a student would Pass or Fail based on their study hours.

**Accuracy:** 50%

### Decision Tree Classifier

A Decision Tree Classifier was trained using a maximum depth of 3. The model learns decision rules from the feature values to classify students.

**Accuracy:** 100%

## Model Comparison

The models were compared using accuracy on the test dataset.

```text
Logistic Regression: 50%
Decision Tree:       100%
````

For this particular experiment, the Decision Tree correctly classified both test samples.

Since the test dataset contained only 2 samples, the accuracy values should be interpreted carefully. This project is intended to demonstrate the classification workflow rather than provide a reliable real-world performance comparison.

## New Data Prediction

Both models were tested with a new student who studied for **7 hours**.

```text
Logistic Regression Prediction: Pass
Decision Tree Prediction: Pass
```

Both models predicted that the student would Pass.

## Evaluation

The following evaluation techniques were used:

* Accuracy Score
* Confusion Matrix
* Classification Report

These metrics helped understand how the models performed on the test data.

## Visualizations

The notebook includes:

* Student classification visualization.
* Model accuracy comparison chart.

## Key Observations

1. Classification predicts categories rather than continuous numerical values.
2. Logistic Regression can be used for binary classification.
3. Decision Trees classify data using feature-based decision rules.
4. The Decision Tree achieved higher accuracy on this particular test set.
5. Model performance should be evaluated using an adequately sized and representative dataset.


