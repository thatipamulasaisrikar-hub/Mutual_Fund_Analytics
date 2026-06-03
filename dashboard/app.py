import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("Mutual Fund Analytics Dashboard")

# Connect to SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load data
nav = pd.read_sql("SELECT * FROM fact_nav", engine)
transactions = pd.read_sql("SELECT * FROM fact_transactions", engine)
performance = pd.read_sql("SELECT * FROM fact_performance", engine)

# Metrics
st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("NAV Records", len(nav))

with col2:
    st.metric("Transactions", len(transactions))

with col3:
    st.metric("Avg NAV", round(nav["nav"].mean(), 2))

# Data Preview
st.header("NAV Data Sample")
st.dataframe(nav.head())

st.header("Transaction Data Sample")
st.dataframe(transactions.head())

st.header("Performance Data Sample")
st.dataframe(performance.head())