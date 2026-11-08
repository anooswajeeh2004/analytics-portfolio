-- Warm-up 6:
-- Which 10 seller cities have the most sellers?
-- Show the city, its state, and the number of sellers.
SELECT
  seller_city,
  seller_state,
  COUNT(*) AS sellers_count
FROM
  sellers
GROUP BY
  seller_city,
  seller_state
ORDER BY
  sellers_count DESC,
  seller_city ASC,
  seller_state ASC
LIMIT
  10;
/*  Results:
 sao paulo	SP	694
 curitiba	PR	124
 rio de janeiro	RJ	93
 belo horizonte	MG	66
 ribeirao preto	SP	52
 guarulhos	SP	50
 ibitinga	SP	49
 santo andre	SP	45
 campinas	SP	41
 maringa	PR	40
\*