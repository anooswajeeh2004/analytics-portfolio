-- How many sellers does each state have? Show only states with at least 50 sellers. Show the most first.
SELECT
  seller_state,
  COUNT(*) AS sellers_count
FROM
  sellers
GROUP BY
  seller_state
HAVING
  COUNT(*) >= 50
ORDER BY
  sellers_count DESC;
/* Result:
SP	1849
1	PR	349
2	MG	244
3	SC	190
4	RJ	171
5	RS	129 
*/
-- (States with 50 or more sellers, ordered by count descending)