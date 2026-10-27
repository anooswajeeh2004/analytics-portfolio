# Day 2 — SQL Past the Basics

## Part 0 — Guess Three Row Counts

| Join                           | My guess | The real count | kind         |
| ------------------------------ | -------- | -------------- | ------------ |
| `orders` with `customers`      | 99,441   | 99441          | one-to-many  |
| `orders` with `order_items`    | 100,000  | 112650         | one-to-many  |
| `customers` with `geolocation` | 100,000  | 15083455       | many-to-many |

## Findings & Takeaways

### 1. Row Counts & The Join Multiplier

- **Key Takeaway:** Joins don't just combine tables; they can cause a multiplication effect on row counts, especially in One-to-Many or Many-to-Many relationships (e.g., customers and geolocation).
- Always estimate row counts and compare them with the real counts before relying on query outputs.

### 2. The Grain of Data

- Every query and result has a specific "grain" (what a single row represents).
- Ignoring the grain leads to severe aggregation errors, such as confusing the average price of an individual item with the average total price of a full order.

### 3. The 3 NULL Dangers

- Mishandling `NULL` values (like using them with `NOT IN` or direct comparisons like `<>`) can silently drop rows or produce misleading results without any error messages.
- **Solution:** Use safer alternatives like `NOT EXISTS` and explicit checks.

### 4. Working with Dates (`::date` & `date_trunc`)

- Using `::date` truncates timestamps for clean date-to-date comparisons, avoiding false positives in late delivery calculations.
- Using `date_trunc` helps easily aggregate and group data by week or month.
