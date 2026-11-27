-- Warm-up 16:
-- On average, how many hours pass between an order's purchase and its approval?
-- Use only orders that have an approval time. Round to 1 decimal.
SELECT
  ROUND(
    AVG(
      EXTRACT(
        EPOCH
        FROM
          (
            order_approved_at - order_purchase_timestamp
          )
      ) / 3600
    )::numeric,
    1
  ) AS avg_approval_hours
FROM
  clean.orders
WHERE
  order_approved_at IS NOT NULL;
-- Result:
-- avg_approval_hours    10.4