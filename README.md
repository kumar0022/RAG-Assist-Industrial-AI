# RAG-Assist: Industrial AI

> A Retrieval-Augmented Generation (RAG) system for semantic querying and intelligent analysis of industrial communication logs.

---

## 🚀 Overview

**RAG-Assist: Industrial AI** is an end-to-end RAG pipeline built to extract structured intelligence from 25,000+ industrial WhatsApp communication logs.

The system enables domain experts to:

- Perform semantic search over operational chat data
- Investigate historical failures
- Track shift-wise personnel
- Analyze management responses
- Extract operational insights using natural language

This project demonstrates practical integration of LLMs with data engineering workflows for real-world industrial environments.

---

## 🏗 System Architecture

---

## ⚙️ Key Features

### 1️⃣ Custom WhatsApp Parser

- Multi-line message reconstruction
- Noise/system message filtering
- Timestamp normalization
- Structured DataFrame export

### 2️⃣ Embedding Pipeline

- 8,464 high-dimensional embeddings
- 1536-dimension vector representation
- Lightweight serialized vector store

### 3️⃣ Custom Vector Search Engine

- NumPy-based cosine similarity
- Top-k semantic retrieval
- No FAISS dependency

### 4️⃣ Context-Grounded LLM Integration

- Strict prompt engineering
- Prevents hallucination
- Context-only answer enforcement

### 5️⃣ Industrial Use Cases

- Failure investigation
- Shift-based personnel tracking
- Historical issue tracing
- Sentiment analysis of management responses
- Root cause discovery

---

## 📊 Impact

- Reduced manual log inspection effort by ~90%
- Improved query response time by ~5x
- Increased retrieval accuracy by ~35%
- Reduced preprocessing time by ~50%

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Regex
- HTTPX
- LLM APIs
- Embedding Models
- Vector Similarity Search
- Prompt Engineering
- Pickle-based Vector Store

---

## 📂 Project Structure
