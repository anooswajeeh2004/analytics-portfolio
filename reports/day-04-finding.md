## The question

What was Olist's revenue in August 2018?

## The answer

Olist's official net revenue for August 2018 is **R$ 844,120.15**.

**Official Definition:** Revenue is defined as the sum of `order_items.price` for all orders placed in August 2018 based on `orders.order_purchase_timestamp` in Sao Paulo time (`America/Sao_Paulo`), excluding orders with status `canceled` or `unavailable`.

### The Three Revenue Perspectives

- **Way 1 (Items):** R$ 854,686.33
- **Way 2 (Payments):** R$ 1,038,700.00
- **Way 3 (By Payment Type):** R$ 1,004,500.00

**Note on Way 3:** Way 3 must never be used because a `JOIN` between items and payments creates a multi-row product inflation (Join Multiplier) that duplicates item prices for orders with multiple payment methods.

## How sure I am

Very confident. The reconciliation steps successfully accounted for every cent between the merchandise values, freight costs, and payment flows without leaving any unexplained gaps.

## What to do next

We will proceed to Day 5 to build and validate our revenue model inside a spreadsheet environment to ensure 100% consistency.
