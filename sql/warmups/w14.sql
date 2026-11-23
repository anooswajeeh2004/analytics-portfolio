-- Warm-up 14:
-- How many orders were placed on each day of the week?
-- Show the day's name. Start with Monday.
SELECT
  TO_CHAR(order_purchase_timestamp, 'FMDay') AS day_name,
  COUNT(*) AS order_count
FROM
  clean.orders
GROUP BY
  EXTRACT(ISODOW
    FROM
      order_purchase_timestamp),
  TO_CHAR(order_purchase_timestamp, 'FMDay')
ORDER BY
  EXTRACT(ISODOW
    FROM
      order_purchase_timestamp);
-- Result:
--  day_name	   order_count
--	Monday	       16196
--	Tuesday	       15963
--	Wednesday	   15552
--	Thursday	   14761
--	Friday	       14122
--	Saturday       10887
--	Sunday	       11960