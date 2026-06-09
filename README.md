# Mutual Fund Analytics

## Project Overview

Mutual Fund Analytics is a data engineering and analytics project that collects, validates, cleans, stores, and analyzes mutual fund data using Python, SQLite, SQL, and Streamlit.

The project demonstrates an end-to-end data pipeline, including data ingestion, data quality validation, data cleaning, database integration, SQL analysis, exploratory data analysis (EDA), performance analytics, and dashboard visualization.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Streamlit
* Git & GitHub

---

## Project Structure

```text
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 02_data_cleaning.ipynb
│   ├── 03_EDA_Analysis.ipynb
│   └── 04_Performance_Analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── app.py
│
├── reports/
│   ├── data_dictionary.md
│   └── data_quality_summary.txt
│
├── create_database.py
├── load_to_sqlite.py
├── check_db.py
├── data_ingestion.py
├── live_nav_fetch.py
├── validate_amfi_codes.py
└── README.md
```

---

## Features

* Data ingestion from multiple mutual fund datasets
* Data validation and quality checks
* Data cleaning and preprocessing
* SQLite database integration
* SQL-based analysis
* Interactive Streamlit dashboard
* Automated reporting
* Exploratory Data Analysis (EDA)
* NAV trend analysis
* SIP inflow analysis
* Investor demographic analysis
* Geographic distribution analysis
* Correlation analysis
* Sharpe Ratio analysis
* Sortino Ratio analysis
* Alpha & Beta calculations
* Maximum Drawdown analysis
* Fund Scorecard generation
* Benchmark comparison analytics

---

## Project Progress

### Day 1 – Data Ingestion ✅

* Data ingestion pipeline
* Live NAV fetch
* AMFI code validation
* GitHub repository setup

### Day 2 – Data Cleaning & Database Integration ✅

* Data cleaning and preprocessing
* SQLite database creation
* Data loading scripts
* SQL schema creation
* Dashboard setup

### Day 3 – Exploratory Data Analysis (EDA) ✅

* NAV trend analysis
* AUM growth analysis
* SIP inflow trend analysis
* Category inflow heatmap
* Investor demographic analysis
* Geographic distribution analysis
* Folio growth analysis
* Correlation matrix
* Sector allocation analysis
* 15+ visualizations created

### Day 4 – Fund Performance Analytics ✅

* Daily return calculations
* CAGR calculations
* Sharpe Ratio ranking
* Sortino Ratio ranking
* Alpha & Beta analysis
* Maximum Drawdown analysis
* Fund Scorecard generation
* Benchmark comparison analysis
* Tracking error calculations

### Day 6 – Advanced Analytics & Risk Metrics ✅

* Historical VaR (95%) and CVaR calculations
* Rolling 90-Day Sharpe Ratio analysis
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System
* Sector Concentration (HHI) Analysis
* Advanced risk insights and reporting

### Additional Deliverables

* 05_Advanced_Analytics.ipynb
* var_cvar_report.csv
* recommender.py
* rolling_sharpe_chart.png

---

## Database Tables

### fact_nav

Stores historical NAV records.

### fact_transactions

Stores investor transaction details.

### fact_performance

Stores mutual fund performance metrics.

---

## Analytics Outputs

### Processed Data

* cleaned_nav_history.csv
* cleaned_investor_transactions.csv
* cleaned_scheme_performance.csv

### Performance Analytics

* alpha_beta.csv
* fund_scorecard.csv
* tracking_error.csv

---

## Key Metrics

* Total NAV Records: 46,000
* Total Transactions: 32,778
* Average NAV: 269.57

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

### Verify Tables

```bash
python check_db.py
```

### Run Dashboard

```bash
python -m streamlit run dashboard/app.py
```

---

## Dashboard

The Streamlit dashboard provides:

* Key business metrics
* NAV data preview
* Investor transaction preview
* Fund performance preview
* SQLite-powered analytics

---

## Exploratory Data Analysis

The EDA notebook includes:

* NAV trend visualization
* SIP inflow trends
* Category inflow heatmaps
* Investor demographics
* Geographic fund distribution
* Folio growth trends
* Correlation analysis
* Sector allocation analysis

---

## Performance Analytics

The performance analytics notebook includes:

* Daily return calculations
* CAGR analysis
* Sharpe Ratio ranking
* Sortino Ratio ranking
* Alpha & Beta estimation
* Maximum Drawdown analysis
* Fund Scorecard generation
* Benchmark comparison analysis

---

## Author

**Sai Srikar**

Data Engineering & Analytics Project
