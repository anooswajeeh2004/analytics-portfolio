## 1. The question

"How much of Olist's item sales come from its biggest sellers?"

## 2. The answer

Item sales are defined as the total number of items sold by sellers across all delivered orders.

- The biggest 1% of sellers account for **21.5%** of all item sales.
- The biggest 10% of sellers account for **61.2%** of all item sales.
- It takes **286** of the biggest sellers (out of 3,095 sellers) to make half (50%) of all item sales.

_Business Takeaway:_ Revenue generation on the Olist platform is heavily concentrated within a small fraction of top-performing vendors. Retention and key account management strategies should heavily target this core seller tier.

## 3. How sure I am

High certainty. The analysis relies on exact window aggregations (`ROW_NUMBER()` and cumulative sum `SUM() OVER ()`) filtered on distinct valid items and sellers within the database.

## 4. What to do next

Implement a priority support program for the top 10% of sellers to minimize churn, and explore vendor onboarding programs to help bottom-tier sellers increase their catalog visibility.
