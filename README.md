# Mutual Fund Analytics

## Project Overview

Mutual Fund Analytics is a data engineering and analytics project that collects, validates, cleans, stores, and analyzes mutual fund data using Python, SQLite, SQL, and Streamlit.

The project demonstrates an end-to-end data pipeline, including data ingestion, data quality validation, data cleaning, database integration, SQL analysis, and dashboard visualization.

---

## Tech Stack

* Python
* Pandas
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
│   └── 02_data_cleaning.ipynb
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

---

## Database Tables

### fact_nav

Stores historical NAV records.

### fact_transactions

Stores investor transaction details.

### fact_performance

Stores mutual fund performance metrics.

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

## Author

Sai Srikar

Data Engineering & Analytics Project
