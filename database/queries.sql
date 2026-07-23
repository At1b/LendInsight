-- Total Customers
SELECT COUNT(*) AS total_customers
FROM loan_data;

-- Average Income
SELECT ROUND(AVG(income),2) AS average_income
FROM loan_data;

-- High Risk Customers
SELECT COUNT(*) AS high_risk_customers
FROM loan_data
WHERE risk_flag = 1;

-- Total States
SELECT COUNT(DISTINCT state) AS total_states
FROM loan_data;

-- Top 10 States
SELECT state,
COUNT(*) AS customers
FROM loan_data
GROUP BY state
ORDER BY customers DESC
LIMIT 10;

-- Top 10 Professions
SELECT profession,
COUNT(*) AS customers
FROM loan_data
GROUP BY profession
ORDER BY customers DESC
LIMIT 10;

-- Risk Percentage by State
SELECT
state,
ROUND(
100.0 * SUM(risk_flag) / COUNT(*),
2
) AS risk_percentage
FROM loan_data
GROUP BY state
ORDER BY risk_percentage DESC;