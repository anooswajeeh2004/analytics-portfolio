# Day 1: Meet the Data - Findings & Reflections

| Table                  | One row is one... (your guess) | The column or columns that are different in every row (your guess) |
| :--------------------- | :----------------------------- | :----------------------------------------------------------------- |
| `orders`               | order                          | `order_id`                                                         |
| `customers`            | customer                       | `customer_id`                                                      |
| `order_items`          | item                           | `order_id`, `order_item_id`                                        |
| `order_payments`       |                                |                                                                    |
| `order_reviews`        |                                |                                                                    |
| `products`             |                                |                                                                    |
| `sellers`              |                                |                                                                    |
| `geolocation`          |                                |                                                                    |
| `category_translation` |                                |                                                                    |

---

## Proven Table & Fact-Checked Definitions

- **`orders`**: One row is one unique order transaction (`order_id`). _(Guess was correct)_
- **`customers`**: One row is a customer-order instance (`customer_id`). _(Guess was correct)_
- **`order_items`**: One row is an individual item within an order. _(Guess was incomplete; missed that it requires a composite primary key: `order_id` + `order_item_id`)_
- **`order_payments`**: One row is a payment installment/record for an order, identified by (`order_id`, `payment_sequential`). _(Guess was left empty as per review instructions)_
- **`order_reviews`**: One row is a customer review instance, identified by (`review_id`, `order_id`). _(Guess was left empty)_
- **`products`**: One row is a unique product catalog item (`product_id`). _(Guess was left empty)_
- **`sellers`**: One row is a unique seller merchant (`seller_id`). _(Guess was left empty)_
- **`geolocation`**: One row is a coordinate point for a zip code prefix. Has no strict primary key as zip codes span multiple coordinates. _(Guess was left empty)_
- **`category_translation`**: One row is a product category mapping from Portuguese to English (`product_category_name`). _(Guess was left empty)_

---

## Errors Seen Today and What They Taught Us

1. **Assuming Single-Column Primary Keys Everywhere:**
   - _Error:_ Initially assumed tables like `order_items`, `order_payments`, and `order_reviews` can rely on a single ID column.
   - _Lesson:_ Learned the critical importance of composite primary keys when tracking granular transactional details like items, installments, or multiple review entries per order.

2. **Treating Geolocation as a Strict Parent Table:**
   - _Error:_ Tried to enforce a direct foreign key constraint on the `geolocation` zip code column.
   - _Lesson:_ Discovered that postal codes span multiple coordinate points and states, resulting in a many-to-many relationship rather than a valid parent-child foreign key lookup.

3. **Jupyter Notebook Caching:**
   - _Error:_ Modified Python backend scripts (like `profile.py`) while keeping the notebook open, resulting in changes not being reflected.
   - _Lesson:_ Understood how Jupyter caches imported modules and why performing a kernel restart (`Restart Kernel`) is necessary when updating external scripts.
