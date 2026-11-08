# Day 2 Finding: Advanced SQL & Delivery Performance Analysis

## The question

What is the true late delivery rate for Olist orders, and how do timestamp precision, date truncation, and NULL handling affect this performance metric?[cite: 8, 12]

## The answer

The standard date-truncated late delivery rate is **6.77%** when comparing calendar dates (`order_delivered_customer_date::date > order_estimated_delivery_date::date`)[cite: 12].

Using exact timestamp comparison increases the reported late rate to **8.11%** because any fraction of a second past the estimated delivery threshold flags the order as late[cite: 12]. Furthermore, evaluating average late delivery rates with `CASE` logic without an `ELSE 0.0` clause yields **7.87%** because SQL `AVG()` ignores `NULL` values, altering the denominator[cite: 12].

## How sure I am

I am completely confident in these figures as they are derived directly from SQL window functions and exact temporal comparisons across the full Olist database[cite: 12]. The variance between 6.77%, 7.87%, and 8.11% clearly illustrates how aggregation methodology and time granularity alter analytical findings[cite: 12].

## What to do next

Align with operational and logistics stakeholders to standardize the official metric definition (whether to use date-truncation or exact timestamps, and how to handle non-delivered orders in the denominator) to ensure consistent performance reporting across departments[cite: 12].
