
# Day 15 — Large Language Models and Hugging Face

## Introduction

On Day 15 of my AI/ML internship, I learned the basics of **Large Language Models (LLMs)** and explored how pretrained AI models can be used for different Natural Language Processing tasks.

I used the Hugging Face Transformers library to test three different AI models for:

- Text Generation
- Sentiment Analysis
- Text Summarization

## Objectives

- Understand the evolution from traditional Machine Learning to Generative AI.
- Understand the basics of Large Language Models.
- Explore the Hugging Face Model Hub.
- Test different pretrained AI models.
- Compare model outputs.
- Record observations based on the different NLP tasks.
- Update the GitHub repository.

## ML and Generative AI Workflow

### Traditional Machine Learning

```text
Data → Features → ML Model → Prediction
````

### Generative AI / LLM

```text
Prompt → Tokenization → Pretrained Model → Generated Output
```

## Models Tested

### 1. Text Generation

**Model:** `openai-community/gpt2`

The model was tested using the prompt:

```text
Artificial intelligence is changing education because
```

The model generated additional text based on the given prompt.

The output was relevant to the input topic, although some repetition was observed in the generated text.

### 2. Sentiment Analysis

**Model:** `distilbert/distilbert-base-uncased-finetuned-sst-2-english`

The model was used to classify text as either Positive or Negative.

Example input:

```text
I really enjoyed this course because the explanations were clear,
practical and easy to understand.
```

The model predicted:

```text
POSITIVE
```

with a high confidence score.

Additional test cases produced:

```text
"The project was excellent and I learned a lot."
→ POSITIVE

"The explanation was confusing and the experience was disappointing."
→ NEGATIVE

"The course was useful and practical."
→ POSITIVE
```

### 3. Text Summarization

**Model:** `sshleifer/distilbart-cnn-12-6`

The model was used to summarize a paragraph about Artificial Intelligence, Machine Learning, Generative AI, Large Language Models, and Hugging Face.

The model produced a shorter version containing the main information from the original text.

## Model Comparison

| Task               | Model      | Observation                                                           |
| ------------------ | ---------- | --------------------------------------------------------------------- |
| Text Generation    | GPT-2      | Generated text based on the prompt, with some repetition              |
| Sentiment Analysis | DistilBERT | Produced clear Positive/Negative classifications with high confidence |
| Summarization      | DistilBART | Generated a shorter version while retaining the main information      |

Since these models perform different tasks, there is no single overall best model. The appropriate model depends on the specific task and the required output.

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Model Hub
* Google Colab
* Git
* GitHub

## Key Takeaways

* LLMs can perform different language-related tasks using pretrained models.
* Hugging Face provides access to many pretrained AI models.
* Transformers makes it easier to load and use pretrained models.
* Text generation, sentiment analysis, and summarization have different objectives.
* Model performance should be evaluated according to the task being performed.

## Project Workflow

```text
Explore Hugging Face
        ↓
Load Pretrained Models
        ↓
Text Generation
        ↓
Sentiment Analysis
        ↓
Text Summarization
        ↓
Compare Outputs
        ↓
Record Observations
```

