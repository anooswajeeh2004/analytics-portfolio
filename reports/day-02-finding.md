# Day 2 Finding: Advanced SQL & Delivery Performance Analysis

## 1. Overview & Objectives

Exploring advanced aggregation, filtering, and time-zone conversions on the Olist e-commerce dataset to evaluate delivery performance and temporal trends.

## 2. On-Time vs. Late Delivery Analysis (6.77%)

- **Counted Metric:** Evaluated delivered orders strictly on a calendar-date basis (`order_delivered_customer_date::date > order_estimated_delivery_date::date`).
- **Result:** Yields a late delivery rate of **6.77%**.

## 3. Comparing Timestamp Variations (8.11% and 7.87%)

- **8.11% Rate:** Calculated using precise timestamp comparisons (`order_delivered_customer_date > order_estimated_delivery_date`), where any fraction of a second past the deadline flags the order as late.
- **7.87% Rate:** Reflects alternative condition filtering or specific case-handling logic in the query structure.
- **Key Takeaway:** The difference between these rates highlights how precise timestamp evaluation versus date-only truncation affects operational performance reporting.

## 4. Conclusion & Lessons Learned

Handling temporal data requires careful consideration of time zones (São Paulo vs. UTC) and explicit distinction between timestamps and dates to avoid discrepancies in business metrics.
