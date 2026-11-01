# Day 3 Finding: Window Functions & Revenue Analysis

## 1. Overview & Objective

Using window functions and aggregations to analyze revenue distribution and seller performance across the Olist platform.

## 2. Revenue-Based Analysis (SUM of Price)

- Counting items alone can be misleading (e.g., counting a low-cost pen the same as an expensive refrigerator). Therefore, we aggregate total monetary value using `SUM(price)` from `order_items`.
- **Top Revenue Generators:** Evaluated top-performing categories and sellers based on actual monetary volume rather than raw item counts.

## 3. Active Seller Metrics

- Out of the total 3,095 registered sellers in the database, exactly **2,970 sellers** have at least one successfully delivered order contributing to actual revenue.
- The query structure precisely filters for active delivered orders to ensure accurate merchant representation.

## 4. Query Verification

The underlying query has been embedded and verified directly within the Day 3 Jupyter Notebook (`notebooks/day-03-window-functions.ipynb`) to ensure full reproducibility.
