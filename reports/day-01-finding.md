## The question

What must every analysis of the Olist data watch out for?

## The answer

Here are the 5 most important things every analysis of the Olist data must watch out for, ordered from most dangerous to least dangerous:

1. **Multi-Payment Row Multiplication (Cartesian Product Inflation):** Joining `order_items` directly with `order_payments` causes row duplication for multi-payment orders, severely inflating revenue and financial figures.
2. **Inclusion of Canceled and Unavailable Orders:** Failing to filter out canceled or unfulfilled orders distorts baseline sales performance and net revenue totals.
3. **Composite Primary Keys:** Assuming single columns like `order_item_id` or `review_id` are unique globally, whereas they restart or repeat across orders and require composite keys.
4. **Unmapped Category Names:** Missing translations or raw Portuguese category names that default to NULL or break category-level reporting groups.
5. **Geolocation Many-to-Many Explosion:** Joining customers or sellers with geolocation tables via zip code prefix alone creates millions of duplicate rows due to multiple coordinate entries per prefix.

## How sure I am

High confidence in these findings based on initial schema audits; however, adding new unlinked historical backfills, changing order status definitions, or modifying seller registration logs could alter these numbers.

## What to do next

Establish a centralized, enterprise-wide data validation guideline and standard SQL query templates for all analytics teams to prevent multi-table join inflation and unfulfilled order distortion in official reporting.
