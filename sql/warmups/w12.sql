-- Warm-up 12:
-- How many orders contain items from more than one seller?
SELECT
  COUNT(*) AS orders_with_multiple_sellers
FROM
  (
    SELECT
      order_id
    FROM
      clean.order_items
    GROUP BY
      order_id
    HAVING
      COUNT(DISTINCT seller_id) > 1
  ) AS multi_seller_orders;
-- Result: [orders_with_multiple_sellers:1278]