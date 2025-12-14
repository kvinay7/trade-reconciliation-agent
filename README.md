# Financial Trade Reconciliation Agent (POC)

A next-generation financial operations agent that combines deterministic logic with Large Language Models (LLMs) to automate the reconciliation of trade records between internal booking systems and external brokers/custodians.

---

## 📖 Overview

**Trade Reconciliation** is the critical process of validating two sets of trade records to ensure every economic trade is correctly recorded, priced, and settled.

Traditional systems rely on brittle, static rules that fail when formats change or fuzzy edge cases (partial fills, symbol aliases) occur. This agent solves that by implementing a **Hybrid Matching Engine**:

* **Deterministic Rules:** For high-speed, high-confidence exact matches.
* **LLM Fuzzy Reasoning:** For complex exceptions, utilizing embeddings and contextual logic to resolve mismatches using contextual similarity comparable to analyst workflows.

---

## ⚡ System Architecture

The system follows a staged ingestion and decision-making pipeline:

1.  **Ingest:** Analyst uploads `internal.csv` and `broker.csv` via UI.
2.  **Parse:** Backend extracts records and prepares them for downstream normalization.
3.  **Deterministic Match:** Rules engine runs exact matches and tolerance checks.
4.  **Fuzzy Match (AI):** Unmatched records undergo vector embedding; the LLM provides a contextual evaluation.
5.  **Hybrid Scoring:** A weighted score determines if the trade is Auto-Matched, Needs Review, or Unmatched.
6.  **Review:** Analyst accepts or rejects matches in the UI.
7.  **Report:** Reconciliation results are exported as Excel reports.

---

## 🛠 Tech Stack

### Core Application
* **Frontend:** Next.js
* **Backend:** Python, Node.js
* **Data Processing:** Pandas

### AI & Reasoning
* **LLM Orchestration:** LangChain
* **Inference & Embeddings:** TogetherAI

### Infrastructure & DevOps
* **DevTools:** CodeRabbit
* **CI/CD:** GitHub Actions
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

    ```bash
        git checkout -b feat/coderabbit
        git add .
        git commit -m "feat: CodeRabbit on PR"
        git push -u origin feat/coderabbit
    ```

---

## 🚀 Release Workflow and Setup

All production changes are merged via Pull Requests with automated CodeRabbit review and Vercel preview deployments.

---

# Implementation

---

## Module 1: Schema-Agnostic CSV Ingestion

### 🎯 Objective

Enable the platform to ingest **any CSV file** (from brokers, custodians, or internal systems) **without predefined schemas, column mappings, or assumptions**. This module establishes the ingestion foundation for downstream normalization, matching, and reconciliation.

### 🧠 Design Principles

* No hardcoded column mappings
* Accept arbitrary CSV formats
* Preserve original headers
* Minimal preprocessing
* Deterministic, testable behavior

---

### 🛠 Implementation Overview

#### 1️⃣ Backend Ingestion

**Location**

```
lib/csv_reader.py
```

**Responsibilities**

* Accept raw CSV file bytes
* Parse data without schema assumptions
* Preserve original column headers
* Apply minimal sanitation only

📌 **Outcome**: Any CSV structure can be ingested safely without brittle ETL logic.

---

#### 2️⃣ Backend Validation

**Location**

```
tests/test_csv_reader.py
```

**Purpose**

* Validate schema-agnostic ingestion behavior
* Ensure:

  * Headers remain unchanged
  * Row counts are accurate
  * No implicit schema enforcement occurs

**Execution**

```bash
python -m tests.test_csv_reader
```

📌 **Outcome**: Deterministic and regression-safe ingestion behavior.

---

#### 3️⃣ Frontend File Upload (Next.js App Router)

**Location**

```
app/page.tsx
```

**Responsibilities**

* Client-side CSV file selection
* Support for multiple file uploads
* No client-side schema validation

📌 **Note**: Implemented as a Client Component to support event handling.

📌 **Outcome**: Frontend remains generic and future-proof.

---

#### 4️⃣ Local End-to-End Verification

**Execution**

```bash
npm run dev
```

**Verification Steps**

1. Open the local development server
2. Upload CSV files with arbitrary headers
3. Confirm uploads complete without runtime errors
4. Ensure backend ingestion tests pass

📌 **Outcome**: Confirms full ingestion flow from UI to backend.

---

### ✅ Result

* Heterogeneous CSV ingestion without schema lock-in
* Clear separation between ingestion and downstream logic
* Testable and reviewable architecture

---

