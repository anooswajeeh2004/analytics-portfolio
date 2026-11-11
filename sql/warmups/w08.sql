-- Which 5 customer states pay the highest average freight per item? Show the state, the average freight rounded to 2 decimals, and the number of items.
SELECT
  c.customer_state,
  ROUND(CAST(AVG(i.freight_value) AS NUMERIC), 2) AS avg_freight,
  COUNT(*) AS item_count
FROM
  order_items i
  JOIN orders o ON i.order_id = o.order_id
  JOIN customers c ON o.customer_id = c.customer_id
GROUP BY
  c.customer_state
ORDER BY
  avg_freight DESC
LIMIT
  5;
/*
Result:
 customer_state | avg_freight | item_count 
----------------+-------------+------------
 RR             |       42.98 |        52
 PB             |       42.72 |        602
 RO             |       41.07 |        278
 AC             |       40.07 |        92
 PI             |       39.15 |        542
*/