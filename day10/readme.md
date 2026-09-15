# Day 10 — Machine Learning and Linear Regression

## AI/ML Internship — Day 10

**Name:** Rajat Murhe  
**GitHub Repository:** [Linkific-Tasks](https://github.com/rajatmurhe/Linkific-Tasks)

---

## 1. Introduction

Day 10 focused on understanding the basic Machine Learning workflow and implementing a simple supervised learning model.

For this task, I learned how Machine Learning uses existing data to learn patterns and make predictions.

I implemented a **Linear Regression** model to predict student marks based on the number of hours studied.

---

## 2. Learning Objectives

The main objectives of this task were:

- Understand how Machine Learning works.
- Learn the basic Machine Learning workflow.
- Understand supervised learning.
- Split data into training and testing sets.
- Train a Linear Regression model.
- Make predictions using the trained model.
- Evaluate the model's performance.
- Update the completed work on GitHub.

---

## 3. Machine Learning Workflow

The basic workflow followed in this project was:

```text
Collect Dataset
      ↓
Explore Data
      ↓
Select Features and Target
      ↓
Split Data
      ↓
Train Model
      ↓
Make Predictions
      ↓
Evaluate Model
      ↓
Predict New Data
````

---

## 4. Dataset

For this project, I created a small student performance dataset containing two variables:

* `Hours_Studied` — number of hours studied
* `Marks` — marks obtained by the student

The objective was to understand whether the number of hours studied can be used to predict student marks.

Example data:

```text
Hours_Studied    Marks
1                35
2                40
3                45
4                50
5                55
6                60
7                68
8                72
9                80
10               88
```

---

## 5. Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab
* Git
* GitHub

---

## 6. Importing Libraries

The required Python libraries were imported for data handling, visualization, and Machine Learning.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
```

---

## 7. Exploring the Dataset

Before training the model, I explored the dataset using functions such as:

```python
df.head()
df.shape
df.info()
df.describe()
```

This helped me understand the structure and values of the dataset.

---

## 8. Selecting Features and Target

I selected:

```python
X = df[["Hours_Studied"]]
y = df["Marks"]
```

Here:

* `X` represents the input feature.
* `y` represents the target value that the model needs to predict.

The model learns the relationship between study hours and marks.

---

## 9. Train-Test Split

The dataset was divided into training and testing data using:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The dataset was split into:

* **8 training samples**
* **2 testing samples**

The training data was used to teach the model, while the testing data was used to evaluate how well the model performs on unseen data.

---

## 10. Training the Linear Regression Model

I created a Linear Regression model using Scikit-learn:

```python
model = LinearRegression()

model.fit(X_train, y_train)
```

The model learned the relationship between the number of hours studied and the marks obtained.

---

## 11. Making Predictions

After training the model, predictions were made using:

```python
y_pred = model.predict(X_test)
```

The predicted values were then compared with the actual testing values.

---

## 12. New Prediction

I also tested the trained model with a new input.

For a student who studies for **7 hours**, the model predicted:

```text
67.8 marks
```

This demonstrates how a trained Machine Learning model can be used to make predictions on new data.

---

## 13. Model Evaluation

I evaluated the model using Mean Squared Error and R² Score.

```python
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

The model achieved:

```text
R² Score: 1.0
```

The R² score indicates how well the model explains the variation in the target values.

Since this project uses a very small dataset, the result should be considered as a learning demonstration rather than a production-level model evaluation.

---

## 14. Regression Line

I visualized the relationship between study hours and marks using a scatter plot and the fitted regression line.

The regression line represents the pattern learned by the model from the training data.

This helped me visually understand how Linear Regression works.

---

## 15. Regression Equation

The model can also be represented using a linear equation:

```text
Marks = Slope × Hours Studied + Intercept
```

The model uses this relationship to estimate marks for a given number of study hours.

---

## 16. Summary

**Algorithm:** Linear Regression
**Training Samples:** 8
**Testing Samples:** 2
**R² Score:** 1.0
**Prediction for 7 Hours of Study:** 67.8 Marks

