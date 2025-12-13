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
* **Inference & Embeddings:** TogetherAI
* **Synthetic Data & Training:** Oumi

### Infrastructure & DevOps
* **Orchestration:** Kestra
* **CI/CD:** GitHub Actions
* **Developer Tools:** Cline CLI, CodeRabbit
* **Deployment:** Vercel

---

## 🧑‍💻 Development

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
