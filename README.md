# Financial Trade Reconciliation Agent

A next-generation financial operations agent that combines deterministic logic with Large Language Models (LLMs) to automate the reconciliation of trade records between internal booking systems and external brokers/custodians.

---

## 📖 Overview

**Trade Reconciliation** is the critical process of validating two sets of trade records to ensure every economic trade is correctly recorded, priced, and settled.

Traditional systems rely on brittle, static rules that fail when formats change or fuzzy edge cases (partial fills, symbol aliases) occur. This agent solves that by implementing a **Hybrid Matching Engine**:

* **Deterministic Rules:** For high-speed, high-confidence exact matches.
* **LLM Fuzzy Reasoning:** For complex exceptions, utilizing embeddings and contextual logic to resolve mismatches like a human analyst would.

---

## 🚀 Key Features

* **Hybrid Matching Logic:** Combines traditional rules with embeddings for a robust matching score.
* **Human-in-the-Loop:** Dashboard allows analysts to review low-confidence matches with LLM-generated explanations.
* **Automated Orchestration:** Pipelines handle the end-to-end flow: Ingest → Parse → Match → Report.
* **Continuous Learning:** Analyst decisions are fed back into the system to synthesize edge cases and improve future model performance.

---

## ⚡ System Architecture

The system follows a strict ETL and decision-making pipeline:

1.  **Ingest:** Analyst uploads `internal.csv` and `broker.csv` via UI.
2.  **Parse:** Backend normalizes data (TradeID, Symbol, Side, Qty, Price, Timestamp).
3.  **Deterministic Match:** Rules engine runs exact matches and tolerance checks.
4.  **Fuzzy Match (AI):** Unmatched records undergo vector embedding; the LLM provides a contextual evaluation.
5.  **Hybrid Scoring:** A weighted score determines if the trade is Auto-Matched, Needs Review, or Unmatched.
6.  **Review:** Analyst accepts or rejects matches in the UI.
7.  **Learn:** Decisions are persisted to retrain the model.

---

## 🛠 Tech Stack

### Core Application
* **Frontend:** Next.js
* **Backend:** Python, Node.js
* **Data Processing:** Pandas

### AI & Reasoning
* **LLM Orchestration:** LangChain
* **Inference & Embeddings:** TogetherAI
* **Synthetic Data & Training:** Oumi

### Infrastructure & DevOps
* **Orchestration:** Kestra
* **CI/CD:** GitHub Actions
* **DevTools:** Cline, CodeRabbit
* **Deployment:** Vercel

---

## 🧑‍💻 Development Setup

* Create GitHub Repository and Codespace

* Verify Environment:
    ```bash
        node -v
        npm -v
        python3 --version
        git --version
    ```

* Scaffold Next.js App (Vercel-Compatible):
    ```bash
        npx create-next-app@latest .
        npm run dev
    ```

* Git Commit:
    ```bash
        git status
        git add .
        git commit -m "init: Next.js app scaffold (Vercel-ready)"
        git push origin main
    ```

* Enable CodeRabbit:
    * Go to GitHub Marketplace
    * Search CodeRabbit
    * Install → Select only this repository
    * Enable auto PR reviews
    * Add `.github/coderabbit.yml`

* Add Cline CLI:
    ```bash
        npm install -g cline
        cline version
        cline auth
    ```

---

# Implementation

## Schema Discovery & Canonical Normalization (LLM-Driven)

### 🎯 Objective

Enable the system to **accept any CSV file without predefined schemas**, automatically infer a **canonical schema using an LLM**, normalize all other files against it, and prepare data for matching.

This removes brittle assumptions and mirrors **real-world financial data onboarding**.

---

### ✅ Key Design Principles

* ❌ No hardcoded column mappings
* ✅ Any CSV format supported
* ✅ User selects a **central (reference) file**
* ✅ LLM infers **semantic meanings** of columns
* ✅ Canonical schema becomes the system’s contract
* ✅ All other files are normalized via LLM reasoning

---

### 🧩 Step-by-Step Implementation

---

### **1. Accept Any CSV (Schema-Agnostic Ingestion)**

The system ingests CSV files **without assuming column names or formats**.

**Implementation**

* Read raw CSV into a Pandas DataFrame
* Preserve original headers
* Perform only minimal cleaning (trim spaces)

**Result**

* Any broker, custodian, or internal format is accepted

---

### **2. Extract Schema Metadata from Central File**

Once the user selects a **central file**, the system extracts metadata for LLM reasoning:

* Column names
* Inferred data types
* Sample rows

This metadata becomes the **input context** for schema inference.

**Why**
LLMs reason better with **structure + examples**, not just headers.

---

### **3. Generate Canonical Schema using LLM (LangChain + Pydantic)**

Using **LangChain**, the extracted schema is sent to the LLM to:

* Infer semantic meaning of each column
* Propose canonical field names
* Generate human-readable descriptions

**Output is strictly validated using Pydantic (`BaseModel`)** to avoid hallucinated formats.

**Canonical Schema Output Includes**

* `canonical_fields`
* `column_mapping` (source → canonical)
* `descriptions`

This schema becomes the **single source of truth** for the rest of the pipeline.

---

### **4. Normalize All Other Files to Canonical Schema**

For each non-central file:

1. Extract its schema metadata
2. Send both:

   * Canonical schema
   * Source file schema
     to the LLM
3. LLM returns a **column mapping**
4. Apply mapping to produce a **normalized DataFrame**

Unmapped or irrelevant columns are ignored.

**Result**
All datasets now share a **common semantic structure**, regardless of original format.

---

### **5. Provider-Agnostic LLM Architecture**

To support multiple LLM providers:

* **API keys** are stored only in `.env`
* **Provider & model config** lives in a separate config file
* LangChain abstracts provider differences
* Switching providers requires **no code changes**

Supported providers:

* Together AI (default)
* OpenAI (optional)

---

### **6. Configuration & Security Separation**

| Concern           | Location             |
| ----------------- | -------------------- |
| API Keys          | `.env`               |
| Model / Provider  | `config/llm.py`      |
| LLM Logic         | `lib/llm/`           |
| Output Validation | Pydantic `BaseModel` |

This ensures:

* Secure secret handling
* Clean CI/CD
* Vercel compatibility

---

