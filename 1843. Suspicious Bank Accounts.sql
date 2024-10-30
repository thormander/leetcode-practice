# Write your MySQL query statement below

WITH cte AS 
(
    SELECT account_id, SUM(amount) AS Total, DATE_FORMAT(day,'%Y%m') AS YearMonth
    FROM Transactions
    WHERE type = 'Creditor'
    GROUP BY account_id, DATE_FORMAT(day,'%Y%m')
),

cte2 AS
(
    SELECT c.account_id,Total,YearMonth,max_income,
           LEAD(YearMonth) OVER(PARTITION BY c.account_id ORDER BY YearMonth) AS nextMonth
    FROM cte c
    LEFT JOIN Accounts a
    ON c.account_id = a.account_id
    WHERE c.Total > a.max_income
)

SELECT DISTINCT cte2.account_id
FROM cte2
WHERE nextMonth - YearMonth = 1


