--Which 5 product categories have the most products listed? Use the English category names. Some products have no English name. Show them as `unknown`.--
SELECT
  COALESCE(t.product_category_name_english, 'unknown') AS category_name,
  COUNT(p.product_id) AS product_count
FROM
  products AS p
  LEFT JOIN category_translation AS t ON p.product_category_name = t.product_category_name
GROUP BY
  category_name
ORDER BY
  product_count DESC
LIMIT
  5