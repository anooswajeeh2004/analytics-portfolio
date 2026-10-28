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