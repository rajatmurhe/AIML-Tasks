# Day 12 — Machine Learning Model Evaluation

## Introduction

On Day 12 of my AI/ML internship, I learned how to evaluate classification models using different performance metrics.

I evaluated the Logistic Regression and Decision Tree models created during Day 11.

## Objectives

- Evaluate Machine Learning models.
- Calculate Accuracy.
- Calculate Precision.
- Calculate Recall.
- Calculate F1 Score.
- Generate Confusion Matrices.
- Generate Classification Reports.
- Compare model performance.
- Understand which metrics are useful for classification.

## Models Evaluated

- Logistic Regression
- Decision Tree Classifier

## Evaluation Metrics

### Accuracy

Measures the overall percentage of correct predictions.

### Precision

Measures how many predicted positive cases were actually positive.

### Recall

Measures how many actual positive cases were correctly identified.

### F1 Score

Provides a balance between Precision and Recall.

### Confusion Matrix

Shows the number of correct and incorrect predictions for each class.

## Results

### Logistic Regression

```text
Accuracy : 50.00%
Precision: 50.00%
Recall   : 100.00%
F1 Score : 66.67%
````

### Decision Tree

```text
Accuracy : 100.00%
Precision: 100.00%
Recall   : 100.00%
F1 Score : 100.00%
```

## Confusion Matrices

Logistic Regression:

```text
[[0 1]
 [0 1]]
```

Decision Tree:

```text
[[1 0]
 [0 1]]
```

## Metric Selection

For this simple Pass/Fail dataset, Accuracy is easy to understand. However, Precision, Recall and F1 Score provide additional information about classification performance.

Using multiple metrics gives a more complete understanding of the model's predictions.

## Important Observation

The test dataset contains only 2 samples. Therefore, the evaluation scores can change significantly based on a single prediction. These results are useful for demonstrating the evaluation process but should not be treated as a reliable real-world model comparison.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab
* GitHub

## Files

```text
day12/
├── README.md
└── day12_model_evaluation.ipynb
```

## Conclusion

This task helped me understand how classification models are evaluated using Accuracy, Precision, Recall, F1 Score and Confusion Matrix.

I also learned that using multiple metrics provides more detailed information than relying only on accuracy.

