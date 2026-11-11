# Day 2 Finding: Advanced SQL & Delivery Performance Analysis

## The question

What is the true late delivery rate for Olist orders, and how do timestamp precision, date truncation, and NULL handling affect this performance metric?

## The answer

The standard date-truncated late delivery rate is **6.77%** when comparing calendar dates (`order_delivered_customer_date::date > order_estimated_delivery_date::date`).

"8.11% and 7.87% both use the timestamp test. 8.11% has no `ELSE`, so `AVG` skips the orders that never arrived. 7.87% has `ELSE 0.0`, so it counts the orders that never arrived as not late. Neither is the course's definition: that is 6.77%, with the date test.
"

## How sure I am

I am completely confident in these figures as they are derived directly from SQL aggregate queries and exact temporal comparisons across the full Olist database. The variance between 6.77%, 7.87%, and 8.11% clearly illustrates how aggregation methodology and time granularity alter analytical findings.

## What to do next

Align with operational and logistics stakeholders to standardize the official metric definition (whether to use date-truncation or exact timestamps, and how to handle non-delivered orders in the denominator) to ensure consistent performance reporting across departments.
