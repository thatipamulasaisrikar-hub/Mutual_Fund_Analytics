-- Top 5 funds by AUM
SELECT *
FROM fund_master
ORDER BY aum DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM nav_history;

-- Total transactions
SELECT COUNT(*)
FROM investor_transactions;

-- Funds with expense ratio < 1%
SELECT *
FROM scheme_performance
WHERE expense_ratio < 1;

-- NAV records count
SELECT COUNT(*)
FROM nav_history;

-- Total NAV records
SELECT COUNT(*) FROM fact_nav;

-- Total transactions
SELECT COUNT(*) FROM fact_transactions;

-- Average NAV
SELECT AVG(nav) FROM fact_nav;

-- Transaction type summary
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Performance statistics
SELECT AVG(return_1y) AS avg_return_1y
FROM fact_performance;