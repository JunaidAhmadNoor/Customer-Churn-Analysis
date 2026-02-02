# Customer Churn Analysis using Power BI

Placement-oriented project: **data cleaning, EDA, Power BI dashboard, and business insights** — no heavy ML required.

---

## Resume title

**Customer Churn Analysis using Power BI**

### Resume bullet (use this)

> Analyzed customer churn data and built an interactive Power BI dashboard to identify high-risk customer segments and revenue loss, enabling data-driven retention strategies.

---

## What this project includes

| Component | Description |
|-----------|-------------|
| **1. Data cleaning & EDA** | Python (Pandas): missing values, duplicates, churn flag, tenure & spend segments |
| **2. Power BI dashboard** | Overall churn rate, churn by contract/tenure/payment, monthly charges vs churn, revenue lost; filters & KPIs |
| **3. Insights & recommendations** | Documented findings and actionable retention recommendations |
| **4. Optional** | Basic churn prediction (Logistic Regression) — only if time allows |

---

## Dataset

Use the **Telco Customer Churn** dataset (Kaggle):

- **Download:** [Kaggle – Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **File:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Place it in:** `data/` folder

---

## Quick start

### 1. Setup

```bash
cd Customer-Churn-Analysis
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Get the data

- Download the CSV from Kaggle and save it as `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`.

### 3. Run cleaning & EDA (Day 1–2)

```bash
python scripts/01_data_cleaning_eda.py
```

- Reads from `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`
- Writes **cleaned data** to `data/churn_cleaned.csv` (use this in Power BI)

### 4. Build dashboard (Day 3–5)

- Open **Power BI Desktop**
- Get data → Text/CSV → select `data/churn_cleaned.csv`
- Follow the step-by-step guide: **[docs/power_bi_dashboard_guide.md](docs/power_bi_dashboard_guide.md)**
- Build: overall churn rate (card), churn by contract/tenure/payment, monthly charges vs churn, revenue lost; add filters (gender, contract)

### 5. Optional: churn prediction (Day 6–7, if time)

```bash
python scripts/02_churn_prediction.py
```

Uses `churn_cleaned.csv`; Logistic Regression only, no deployment.

### 6. Document insights (Day 6)

- Fill `docs/insights_and_recommendations.md` with your dashboard findings and recommendations.

---

## 7-day crash plan

| Days | Focus |
|------|--------|
| **Day 1–2** | Understand dataset, clean data, basic EDA |
| **Day 3–5** | Build Power BI dashboard, add filters & KPIs |
| **Day 6** | Write insights & recommendations, prepare interview story |
| **Day 7** | Polish resume, add dashboard screenshots to GitHub/Drive |

---

## Project structure

```
Customer-Churn-Analysis/
├── data/                    # Put Telco CSV here; cleaned output here too
├── scripts/
│   ├── 01_data_cleaning_eda.py   # Cleaning + segments + EDA summary
│   └── 02_churn_prediction.py   # Optional logistic regression
├── docs/
│   └── insights_and_recommendations.md
├── requirements.txt
└── README.md
```

---

## Skills you can talk about

- Power BI / Tableau  
- SQL (basic to intermediate)  
- Data cleaning (Pandas)  
- Business analysis & stakeholder storytelling  

Good luck with placements.
