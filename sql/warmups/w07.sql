-- Warm-up 7: Some orders have a customer delivery date, but they are not delivered. How many are there? Show them per status.
SELECT
  order_status,
  COUNT(*) AS order_count
FROM
  orders
WHERE
  order_status != 'delivered'
  AND order_delivered_customer_date IS NOT NULL
GROUP BY
  order_status
ORDER BY
  order_count DESC;
/* Results:
+--------------+-------------+
| order_status | order_count |
+--------------+-------------+
| canceled     |           6 |
+--------------+-------------+
*/