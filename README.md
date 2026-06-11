# Mutual Fund Analytics

## Overview

Mutual Fund Analytics is an end-to-end Data Engineering and Analytics project developed during the Bluestock Data Engineering & Analytics Internship. The project focuses on collecting, processing, analyzing, and visualizing mutual fund data to generate actionable investment insights.

The solution integrates ETL pipelines, SQLite database management, exploratory data analysis, financial performance analytics, risk modeling, investor behavior analysis, recommendation systems, and interactive Power BI dashboards.

---

## Project Objectives

* Build a complete ETL pipeline for mutual fund datasets.
* Clean, validate, and transform financial data.
* Store processed data in SQLite.
* Perform exploratory data analysis (EDA).
* Evaluate fund performance using financial metrics.
* Calculate advanced risk metrics such as VaR and CVaR.
* Analyze investor behavior and SIP continuity.
* Develop interactive dashboards for business intelligence.

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* SQL
* Streamlit
* Power BI
* Git & GitHub

---

## Project Architecture

Raw Data
↓
Data Validation
↓
Data Cleaning & Transformation
↓
SQLite Database
↓
EDA & Financial Analytics
↓
Risk Modeling
↓
Power BI Dashboard & Reports

---

## Key Features

### Data Engineering

* Data ingestion pipeline
* AMFI code validation
* Data cleaning and preprocessing
* SQLite database integration
* SQL-based analysis

### Exploratory Data Analysis

* NAV trend analysis
* SIP inflow analysis
* Investor demographics
* Geographic distribution
* Correlation analysis

### Performance Analytics

* CAGR calculations
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Fund Scorecard

### Advanced Risk Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System

### Dashboard Analytics

* Industry Overview
* Fund Performance
* Investor Analytics
* SIP & Market Trends

---

## Project Structure

```text
Mutual_Fund_Analytics/
│
├── dashboard/
│   ├── app.py
│   ├── Mutual_Fund_Analytics_Dashboard.pbix
│   └── Dashboard.pdf
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 02_data_cleaning.ipynb
│   ├── 03_EDA_Analysis.ipynb
│   ├── 04_Performance_Analytics.ipynb
│   └── 05_Advanced_Analytics.ipynb
│
├── reports/
│   ├── Final_Report.pdf
│   ├── rolling_sharpe_chart.png
│   └── data_quality_summary.txt
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── recommender.py
├── create_database.py
├── load_to_sqlite.py
├── data_ingestion.py
├── validate_amfi_codes.py
├── requirements.txt
└── README.md
```

---

## Key Deliverables

### Analytics Outputs

* alpha_beta.csv
* fund_scorecard.csv
* tracking_error.csv
* var_cvar_report.csv

### Dashboard Deliverables

* Mutual_Fund_Analytics_Dashboard.pbix
* Dashboard.pdf

### Advanced Analytics Deliverables

* 05_Advanced_Analytics.ipynb
* recommender.py
* rolling_sharpe_chart.png

### Final Submission

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Database

```bash
python create_database.py
```

### Load Data

```bash
python load_to_sqlite.py
```

### Verify Database

```bash
python check_db.py
```

### Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Business Impact

This project demonstrates how data engineering, financial analytics, and business intelligence can be combined to transform raw mutual fund data into meaningful insights for investors and financial institutions.

The developed analytics framework supports performance evaluation, risk assessment, investor behavior analysis, and investment decision-making.

---

## Author

**Sai Srikar Thatipamula**

Bluestock Data Engineering & Analytics Internship

2026
