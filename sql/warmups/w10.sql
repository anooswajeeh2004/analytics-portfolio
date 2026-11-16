-- Warm-up 10:
-- Question: How many orders contain more than 3 items?
SELECT
  COUNT(*) AS orders_with_more_than_3_items
FROM
  (
    SELECT
      order_id
    FROM
      clean.order_items
    GROUP BY
      order_id
    HAVING
      COUNT(*) > 3
  ) AS orders_over_3;
-- Result:
--	orders_with_more_than_3_items : 965