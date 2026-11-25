-- Warm-up 15:
-- Which 3 hours of the day have the most orders?
SELECT
  EXTRACT(HOUR
    FROM
      order_purchase_timestamp) AS hour,
  COUNT(*) AS total_orders
FROM
  clean.orders
GROUP BY
  hour
ORDER BY
  total_orders DESC
LIMIT
  3;
-- Result:
--  hour	total_orders
--	16.0	6675
--	11.0	6578
--	14.0	6569