import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

nav = pd.read_csv("data/processed/cleaned_nav_history.csv")
investor = pd.read_csv("data/processed/cleaned_investor_transactions.csv")
scheme = pd.read_csv("data/processed/cleaned_scheme_performance.csv")

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
investor.to_sql("fact_transactions", engine, if_exists="replace", index=False)
scheme.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")