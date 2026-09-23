# DAY 17 — AI/ML INTERNSHIP REPORT

## AI/ML Internship — Day 17

**Name:** Rajat Murhe
**GitHub Repository:** [Linkific-Tasks](https://github.com/rajatmurhe/Linkific-Tasks)

## Introduction

On Day 17, I worked on building a **complete RAG API using FastAPI**.

The objective was to convert the RAG concepts learned previously into an API-based application where a user can upload a PDF, ask questions about the document, and receive AI-generated answers based on the retrieved document content.

I also implemented robustness testing to check how the API behaves with different file types, empty files, invalid PDFs, empty questions, and large documents.

## What I Learned

* Basics of FastAPI.
* How file uploads work through APIs.
* How to extract text from PDF documents.
* How to divide documents into chunks.
* How to attach metadata such as filename, page number, and chunk ID.
* How to generate embeddings from document chunks.
* How to build a FAISS vector index.
* How to perform semantic retrieval.
* How to connect retrieved context with an LLM.
* How to expose a RAG pipeline through API endpoints.
* How to test API robustness and handle invalid inputs.

## Project: FastAPI RAG Document Question Answering API

### Project Objective

The project allows users to:

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the document into chunks.
4. Generate embeddings for the chunks.
5. Store the embeddings in a FAISS index.
6. Ask questions about the uploaded document.
7. Retrieve relevant document chunks.
8. Pass the retrieved context to an LLM.
9. Receive an AI-generated answer along with source information.

## Document Processing

### PDF File Upload

The API accepts PDF files through the `/upload` endpoint.

Before processing the document, the API validates:

* File extension.
* Empty file condition.
* Maximum file size.
* PDF validity.
* Availability of extractable text.

### Text Extraction

I used `pypdf` to extract text page by page from the uploaded PDF.

This also allows page-level metadata to be associated with each retrieved chunk.

### Chunking

The extracted text is divided into smaller chunks using a defined chunk size and overlap.

This makes the document easier to process and improves semantic retrieval.

### Metadata

Each chunk is stored with metadata including:

* Filename
* Page number
* Chunk ID

This metadata can later be returned as the source of the generated answer.

## Embeddings

I used the Sentence Transformer model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The extracted document chunks are converted into numerical embedding vectors.

These embeddings are then used for similarity-based retrieval.

## Vector Search

I used **FAISS** to create a vector index for the document embeddings.

When a user asks a question, the question is converted into an embedding and compared with the stored document vectors to retrieve the most relevant chunks.

## LLM Integration

I used:

```text
google/flan-t5-small
```

as the language model.

The retrieved document chunks are added to the prompt as context, and the model is instructed to answer using the provided document information.

## API Endpoints

The application contains the following endpoints:

### `GET /`

Provides a basic API status response.

### `GET /health`

Checks whether the API is healthy and whether a document has been loaded.

### `POST /upload`

Accepts a PDF file, extracts its content, creates chunks and embeddings, and builds the FAISS index.

### `POST /ask`

Accepts a user question, retrieves relevant document chunks, sends the context to the LLM, and returns the generated answer along with source metadata.

## Complete RAG API Workflow

```text
PDF Upload
     ↓
PDF Text Extraction
     ↓
Document Chunking
     ↓
Metadata Creation
     ↓
Embeddings
     ↓
FAISS Vector Index
     ↓
User Question
     ↓
Query Embedding
     ↓
Semantic Retrieval
     ↓
Relevant Context
     ↓
LLM
     ↓
AI Answer + Sources
```

## Robustness Testing

I designed tests to evaluate how the API handles different types of input.

The testing included:

* Valid PDF file.
* Empty question.
* Unsupported TXT file.
* Unsupported DOCX file.
* Empty PDF file.
* Invalid PDF file.
* Large PDF document.

The API was designed to return appropriate error responses instead of processing invalid inputs.

## Testing Report

The robustness testing was performed to identify how the system behaves under invalid and unusual conditions.

The tests specifically focused on:

* Input validation.
* File-type validation.
* Empty input handling.
* Invalid PDF handling.
* File-size restrictions.
* Large document processing.
* Question validation.

The resulting API responses and screenshots will be included as part of the testing deliverables.

## Improvement Suggestions

Based on the current implementation, the following improvements can be made:

* Add authentication and authorization.
* Support additional document formats such as DOCX and TXT.
* Add OCR support for scanned PDFs.
* Use background workers for large document processing.
* Persist FAISS indexes instead of keeping them only in memory.
* Maintain separate indexes for different users and documents.
* Add stronger hallucination detection and answer validation.
* Add API rate limiting and monitoring.
* Store documents and metadata in persistent storage.
* Use a production-ready persistent vector database such as PostgreSQL with pgvector.

## Challenges Faced

* Integrating PDF processing with the FastAPI workflow.
* Managing document chunks and metadata.
* Connecting embeddings with FAISS retrieval.
* Integrating the retrieved context with the LLM.
* Handling invalid file uploads and empty inputs.
* Designing robustness tests for different failure conditions.

## Key Takeaways

* FastAPI can be used to expose an AI pipeline through REST APIs.
* PDF processing is an important part of document-based RAG systems.
* Metadata makes retrieved information easier to trace back to the original document.
* API validation is important for handling invalid inputs safely.
* Robustness testing helps identify weaknesses in an AI application.
* A RAG system can be converted from a notebook prototype into an API-based application.

## GitHub Update

The Day 17 FastAPI RAG implementation, testing report, and supporting documentation were prepared for upload to the `day17` folder in the **Linkific-Tasks** repository.

