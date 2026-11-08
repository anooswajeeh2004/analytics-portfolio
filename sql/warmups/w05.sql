-- Warm-up 5. For each payment type, how many different orders used it? What percent of all paid orders is that? Round to 1 decimal.
SELECT
  payment_type,
  COUNT(DISTINCT order_id) AS orders_count,
  ROUND(
    100.0 * COUNT(DISTINCT order_id) / (
      SELECT
        COUNT(DISTINCT order_id)
      FROM
        order_payments
    ),
    1
  ) AS pct_of_total
FROM
  order_payments
GROUP BY
  payment_type
ORDER BY
  orders_count DESC
  /* Results:
- credit_card: 76.9%
- boleto: 19.9%
- voucher: 3.9%
- debit_card: 1.5%
- not_defined: 0.0%

   The percentages add up to 102.2% because some orders 
   were paid using more than one payment method,
   causing them to be counted under multiple payment types. */