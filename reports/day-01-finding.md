## The question

What are the structure, scale, and primary keys of the tables comprising the Olist e-commerce dataset?

## The answer

The Olist dataset consists of **9 core relational tables** capturing commercial activity in Brazil from September 2016 to October 2018.

- **Scale:** Contains 99,441 orders, 112,650 order items, 32,951 products, and 99,441 customer-order instances.
- **Key Findings:** Each table relies on specific primary keys (e.g., `order_id` for orders, composite key `order_id, order_item_id` for order items, and `product_id` for products) which form the relational backbone for all subsequent revenue and delivery analyses.

## How sure I am

100% confident. Initial guesses regarding primary and composite keys have been thoroughly audited, verified against database constraints, and reconciled with exact table row counts during our schema profiling phase.

## What to do next

Proceed to Day 2 to apply advanced SQL filtering, window aggregations, and time-zone conversions to evaluate delivery performance and temporal trends across the validated schema.
