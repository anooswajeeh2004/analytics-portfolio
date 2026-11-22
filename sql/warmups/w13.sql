-- Warm-up 13:
-- What is the average review score when delivery is late
-- compared with on-time delivery?
-- Show the number of reviews in each group.
SELECT
  CASE
    WHEN o.order_delivered_customer_date::date > o.order_estimated_delivery_date::date THEN 'late'
    ELSE 'on_time'
  END AS delivery_status,
  ROUND(AVG(r.review_score)::numeric, 2) AS avg_review_score,
  COUNT(*) AS review_count
FROM
  clean.orders AS o
  JOIN clean.order_reviews AS r ON r.order_id = o.order_id
WHERE
  o.order_delivered_customer_date IS NOT NULL
  AND o.order_estimated_delivery_date IS NOT NULL
  AND o.order_status = 'delivered'
GROUP BY
  1
ORDER BY
  delivery_status;
-- Result:
-- late: average review score = 2.27, reviews = 6409
-- on_time: average review score = 4.29, reviews = 89944