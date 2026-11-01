--What percent of all reviews give 5 stars? Round to 1 decimal.
SELECT
  ROUND(
    100.0 * COUNT(*) FILTER (
      WHERE
        review_score = 5) / COUNT(*),
    1
  ) AS pct_5_star_reviews
FROM
  order_reviews;
-- Result:
-- 57.7