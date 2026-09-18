# Day 13 — Natural Language Processing and TF-IDF

## Introduction

On Day 13 of my AI/ML internship, I learned the basics of **Natural Language Processing (NLP)** and implemented fundamental text preprocessing techniques using Python.

The main objective was to understand how raw text can be cleaned, processed, and converted into numerical features that can be used by Machine Learning algorithms.

## Objectives

- Understand the basics of Natural Language Processing.
- Perform text preprocessing.
- Convert text to lowercase.
- Perform tokenization.
- Remove stopwords.
- Apply TF-IDF vectorization.
- Analyze TF-IDF output.
- Visualize important words.

## Dataset

A small text dataset containing sentences related to:

- Machine Learning
- Natural Language Processing
- Artificial Intelligence
- Deep Learning
- Data Analysis

was created for this task.

## Text Preprocessing

### 1. Lowercasing

All text was converted to lowercase so that words with different capitalization were treated consistently.

Example:

```text
Machine Learning
````

becomes:

```text
machine learning
```

### 2. Tokenization

The sentences were split into individual words or tokens.

Example:

```text
machine learning is useful
```

becomes:

```text
["machine", "learning", "is", "useful"]
```

### 3. Stopword Removal

Common English words such as `is`, `the`, `and`, `for`, and `to` were removed using Scikit-learn's English stopword list.

This reduces words that generally provide less useful information for basic text analysis.

### 4. TF-IDF Vectorization

The cleaned text was converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

TF-IDF assigns higher importance to words that are more relevant to a particular document while considering how frequently those words occur across the complete dataset.

## NLP Pipeline

```text
Raw Text
   ↓
Lowercasing
   ↓
Tokenization
   ↓
Stopword Removal
   ↓
Processed Text
   ↓
TF-IDF Vectorization
   ↓
Numerical Feature Matrix
```

## TF-IDF Output

The notebook generated:

* TF-IDF feature names.
* TF-IDF numerical matrix.
* TF-IDF scores for individual documents.
* Top important words based on TF-IDF scores.
* Visualization of the most important words.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Google Colab
* Git
* GitHub

## Key Observations

* Text preprocessing makes raw text more suitable for analysis.
* Lowercasing ensures consistency between words.
* Tokenization breaks text into smaller units for processing.
* Stopword removal reduces common words that may provide limited information.
* TF-IDF converts text into numerical features that can be used by Machine Learning models.
* TF-IDF is a feature extraction technique, not a classification algorithm.

## Challenges Faced

* Understanding the purpose of each preprocessing step.
* Converting sentences into individual tokens.
* Selecting and removing common stopwords.
* Understanding how TF-IDF assigns numerical importance to words.
* Interpreting the resulting TF-IDF matrix.

## Conclusion

This task provided a practical introduction to Natural Language Processing. I learned how to preprocess raw text and convert it into numerical features using TF-IDF.

The complete workflow helped me understand how textual data can be prepared for further Machine Learning and NLP tasks such as text classification and sentiment analysis.


```
