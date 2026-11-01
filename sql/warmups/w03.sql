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
-- Result:
-- SP: 18492, MG: 2448, SC: 1904, RJ: 1711, PR: 725, RS: 593, DF: 189, GO: 173, ES: 104, BA: 99, CE: 63, PE: 54
-- (States with 50 or more sellers, ordered by count descending)