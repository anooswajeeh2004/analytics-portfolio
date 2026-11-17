-- Warm-up 11:
-- Question: Which 5 product categories have the highest
-- freight as a percentage of total price?
-- Only include categories with at least 100 items.
SELECT
  INITCAP(REPLACE (p.category, '_', ' ')) AS category,
  COUNT(*) AS items,
  ROUND(
    (
      SUM(i.freight_value)::numeric / NULLIF(SUM(i.price)::numeric, 0)
    ) * 100,
    1
  ) AS freight_pct
FROM
  clean.order_items AS i
  JOIN clean.products AS p ON p.product_id = i.product_id
GROUP BY
  p.category
HAVING
  COUNT(*) >= 100
ORDER BY
  freight_pct DESC
LIMIT
  5;
-- Result:
--  category	            items	freight_pct
--  Christmas Supplies	    153   	36.7
--	Signaling And Security	199	    30.3
--	Food Drink	            278 	29.7
--	Electronics	            2767	29.1
--	Furniture Living Room	503	    26.1