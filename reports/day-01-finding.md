# Day 1 Finding: Olist Database Structure & Primary Key Analysis

## 1. Overview & Objectives

The objective of Day 1 was to explore the Olist e-commerce database, uncover the underlying data architecture, verify primary and foreign keys, and identify structural anomalies across all 9 core tables.

## 2. Key Findings & Primary Keys

- Successfully verified 8 primary keys and 6 foreign key relationships across the transactional and relational tables.
- Discovered that transactional tables like `order_items`, `order_payments`, and `order_reviews` require **composite primary keys** (e.g., `order_id` combined with a sequence or item ID) to ensure uniqueness.
- Confirmed that core dimension tables (`products` and `sellers`) have zero orphaned records, proving strong referential integrity.

## 3. Data Anomalies & Structural Observations

- **Geolocation Table:** Found that the `geolocation` table lacks a strict primary key because postal codes span multiple coordinate points and states, resulting in a many-to-many relationship.
- **Category Translations:** Identified 610 products with missing category translations, highlighting data sparsity in secondary lookup tables.

## 4. Conclusion & Next Steps

Understanding the structural constraints and primary key definitions provides a solid foundation for writing complex analytical queries in Day 2, ensuring accurate joins and reliable aggregations.
