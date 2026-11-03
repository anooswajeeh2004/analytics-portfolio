-- Warm-up 5. For each payment type, how many different orders used it? What percent of all paid orders is that? Round to 1 decimal.
SELECT
  payment_type,
  COUNT(DISTINCT order_id) AS orders_count,
  ROUND(
    100.0 * COUNT(DISTINCT order_id) / SUM(COUNT(DISTINCT order_id)) OVER (),
    1
  ) AS pct_of_total
FROM
  order_payments
GROUP BY
  payment_type
ORDER BY
  orders_count DESC;
/* Results:
- credit_card: 75.2%
- boleto: 19.5%
- voucher: 3.8%
- debit_card: 1.5%
- not_defined: 0.0%