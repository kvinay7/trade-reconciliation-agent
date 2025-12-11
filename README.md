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

* **Hybrid Matching Logic:** Combines traditional Pandas-based rules with TogetherAI embeddings for a robust matching score.
* **Human-in-the-Loop:** A Streamlit dashboard allows analysts to review low-confidence matches with LLM-generated explanations.
* **Automated Orchestration:** Kestra pipelines handle the end-to-end flow: Ingest → Parse → Match → Report.
* **Continuous Learning:** Analyst decisions are fed back into the system (via Oumi) to synthesize edge cases and improve future model performance.
* **Modern Dev Stack:** Built with speed in mind using Cline for scaffolding and CodeRabbit for automated PR reviews.

---

## ⚡ System Architecture

The system follows a strict ETL and decision-making pipeline:

1.  **Ingest:** Analyst uploads `internal.csv` and `broker.csv` via Streamlit.
2.  **Parse:** Backend normalizes data (TradeID, Symbol, Side, Qty, Price, Timestamp).
3.  **Deterministic Match:** Rules engine runs exact matches and tolerance checks.
4.  **Fuzzy Match (AI):** Unmatched records undergo vector embedding; the LLM provides a contextual evaluation.
5.  **Hybrid Scoring:** A weighted score determines if the trade is Auto-Matched, Needs Review, or Unmatched.
6.  **Review:** Analyst accepts or rejects matches in the UI.
7.  **Learn:** Decisions are persisted to retrain the model.

---

## 🛠 Tech Stack

### Core Application
* **Frontend:** Streamlit 
* **Backend:** Python (Flask)
* **Data Processing:** Pandas, SQLite

### AI & Reasoning
* **Inference & Embeddings:** TogetherAI
* **Synthetic Data & Training:** Oumi
* **Logic:** Hybrid Scoring 

### Infrastructure & DevOps
* **Orchestration:** Kestra
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Developer Tools:** Cline CLI, CodeRabbit

---

