# Day 2 Finding: Advanced SQL & Delivery Performance Analysis

## The question

What is the true late delivery rate for Olist orders, and how do timestamp precision, date truncation, and NULL handling affect this performance metric?

## The answer

The standard date-truncated late delivery rate is **6.77%** when comparing calendar dates (`order_delivered_customer_date::date > order_estimated_delivery_date::date`).

Using exact timestamp comparison without an `ELSE 0.0` clause in the `CASE` statement increases the reported late rate to **8.11%** because SQL `AVG()` ignores `NULL` values, altering the denominator. Adding `ELSE 0.0` correctly accounts for all rows, yielding **7.87%**.

## How sure I am

I am completely confident in these figures as they are derived directly from SQL aggregate queries and exact temporal comparisons across the full Olist database. The variance between 6.77%, 7.87%, and 8.11% clearly illustrates how aggregation methodology and time granularity alter analytical findings.

## What to do next

Align with operational and logistics stakeholders to standardize the official metric definition (whether to use date-truncation or exact timestamps, and how to handle non-delivered orders in the denominator) to ensure consistent performance reporting across departments.
