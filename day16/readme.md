
# Day 16 — Basic RAG Pipeline and Chunk Size Analysis

## Introduction

On Day 16 of my AI/ML internship, I built a basic **Retrieval-Augmented Generation (RAG)** system using company documentation.

The project demonstrates how documents can be divided into chunks, converted into embeddings, stored for vector search, retrieved based on semantic similarity, and provided to an LLM to generate context-aware answers.

I also experimented with different document chunk sizes and evaluated their effect on response quality.

## Objectives

- Understand embeddings.
- Understand vector databases and vector search.
- Implement FAISS.
- Implement ChromaDB.
- Perform semantic search.
- Build a basic RAG pipeline.
- Connect retrieved context with an LLM.
- Compare different document chunk sizes.
- Evaluate generated responses.

## Project Overview

A fictional company knowledge base for **NovaTech Solutions** was created containing information about:

- Customer support
- Product plans
- Refund and cancellation policies
- Remote work
- Leave policy
- Security policy
- Internship program
- Engineering technologies
- Pricing changes
- Data privacy

## RAG Pipeline

```text
Company Documentation
        ↓
Document Chunking
        ↓
Embeddings
        ↓
FAISS / ChromaDB
        ↓
Semantic Search
        ↓
Relevant Context
        ↓
LLM
        ↓
Generated Answer
````

## Document Chunking

Three different chunk sizes were tested:

```text
100 words → 5 chunks
200 words → 3 chunks
400 words → 2 chunks
```

The purpose was to understand how chunk size affects retrieval quality and the final generated response.

## Embeddings

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The document chunks were converted into numerical embedding vectors.

For the 100-word chunks, the embedding matrix contained:

```text
5 chunks × 384 dimensions
```

## Vector Search

### FAISS

FAISS was used to create a vector index and perform similarity search over the document embeddings.

### ChromaDB

ChromaDB was also used to create a collection and store the document chunks for vector-based retrieval.

## Semantic Search

The semantic search function converts the user's question into an embedding and searches the FAISS index for the most relevant document chunks.

For example:

```text
Question:
What are the working hours for customer support?
```

The system retrieves relevant document chunks based on semantic similarity.

## LLM Integration

The project uses:

```text
google/flan-t5-small
```

The retrieved document chunks are provided to the LLM as context.

The prompt instructs the model to answer using only the information provided in the retrieved context.

## Chunk Size Performance Analysis

Five questions were tested across the three chunk sizes:

* Customer support working hours
* Professional plan pricing
* Paid leave days
* Security requirements
* Internship duration

Each response was evaluated using:

* Relevance
* Completeness
* Groundedness

## Results

The experiment showed that the 100-word chunks produced the best overall response quality for the tested questions.

```text
Best Chunk Size: 100 words
Overall Evaluation Score: 0.767
```

The larger 200-word and 400-word chunks frequently produced incomplete or unrelated answers, while the 100-word chunks provided more focused retrieval for this document and question set.

## Key Observations

* Smaller chunks can provide more focused retrieval.
* Larger chunks may contain more information but can reduce retrieval precision.
* Retrieval quality directly affects the quality of the final LLM response.
* Chunk size should be selected based on the document structure and application requirements.
* RAG combines retrieval with generation to provide answers based on external context.

## Technologies Used

* Python
* Pandas
* NumPy
* Sentence Transformers
* FAISS
* ChromaDB
* Hugging Face Transformers
* FLAN-T5
* Google Colab
* Git
* GitHub

## Challenges Faced

* Understanding how embeddings represent documents numerically.
* Implementing vector similarity search.
* Connecting retrieval results with an LLM.
* Comparing different chunk sizes.
* Evaluating the quality of generated responses.
* Handling cases where the LLM produced incomplete answers.

## Key Takeaways

* Embeddings convert text into numerical representations.
* FAISS enables efficient similarity search over embeddings.
* ChromaDB can be used as a vector storage and retrieval system.
* Semantic search retrieves information based on meaning rather than exact keyword matching.
* RAG provides an effective way to combine document retrieval with LLM generation.
* Chunk size is an important factor in RAG performance.



