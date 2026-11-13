--How many products weigh more than 10 kg? What percent of the products with a known weight is that? Round to 1 decimal.
SELECT
  COUNT(*) FILTER (
    WHERE
      product_weight_g > 10000) AS heavy_products_count,
  COUNT(*) AS total_known_weight,
  ROUND(
    CAST(
      100.0 * COUNT(*) FILTER (
        WHERE
          product_weight_g > 10000
      ) / COUNT(*) AS NUMERIC
    ),
    1
  ) AS percentage
FROM
  products
WHERE
  product_weight_g IS NOT NULL;
/*
results:

heavy_products_count: 1891	
total_known_weight: 32949
percentage: 5.7%

*/