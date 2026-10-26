-- How many orders were placed in each year? Show one row per year, oldest first.
SELECT
  EXTRACT(YEAR
    FROM
      order_purchase_timestamp) AS order_year,
  COUNT(*) AS total_orders
FROM
  orders
GROUP BY
  order_year
ORDER BY
  order_year ASC;
-- Result:
-- 2016 | 329
-- 2017 | 45101
-- 2018 | 54011