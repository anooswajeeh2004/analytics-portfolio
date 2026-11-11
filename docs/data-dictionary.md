# Olist Data Dictionary

This document provides a comprehensive dictionary of all tables, columns, data types, descriptions, null counts, and analytical notes for the Olist e-commerce dataset.

---

## 1. orders

- **Grain:** One row per unique order.
- **Key:** `order_id` (99,441 unique values, Primary Key).
- **Total Rows:** 99,441
- **Links:** Links to `customers` (`customer_id`), `order_items`, `order_payments`, and `order_reviews`.

| Column Name                     | Data Type | Nulls | Description & Notes                                       |
| :------------------------------ | :-------- | :---- | :-------------------------------------------------------- |
| `order_id`                      | text      | 0     | Unique identifier of the order. Primary Key.              |
| `customer_id`                   | text      | 0     | Key to the customer table instance.                       |
| `order_status`                  | text      | 0     | Status of the order (delivered, shipped, canceled, etc.). |
| `order_purchase_timestamp`      | timestamp | 0     | Time the order was purchased (São Paulo local time).      |
| `order_approved_at`             | timestamp | 160   | Timestamp when payment approval was registered.           |
| `order_delivered_carrier_date`  | timestamp | 1,783 | Timestamp when order was handed over to the carrier.      |
| `order_delivered_customer_date` | timestamp | 2,965 | Actual delivery timestamp to the customer.                |
| `order_estimated_delivery_date` | timestamp | 0     | Estimated delivery date at purchase time.                 |

- **Date:** All times are São Paulo time, with your proof: 666 orders from 03:00 to 06:00, and 4,700 from 06:00 to 09:00.
- **order_estimated_delivery_date:** order_estimated_delivery_date is a date. Compare it only with dates.

---

## 2. customers

- **Grain:** One row per customer profile per order instance.
- **Key:** `customer_id` (99,441 unique values, Primary Key).
- **Total Rows:** 99,441
- **Links:** Links to `orders` (`customer_id`) and `geolocation` (`customer_zip_code_prefix`).

| Column Name                | Data Type | Nulls | Description & Notes                                              |
| :------------------------- | :-------- | :---- | :--------------------------------------------------------------- |
| `customer_id`              | text      | 0     | Key to the order instance. Primary Key.                          |
| `customer_unique_id`       | text      | 0     | Actual unique customer identifier (used to track repeat buyers). |
| `customer_zip_code_prefix` | text      | 0     | First 5 digits of customer zip code.                             |
| `customer_city`            | text      | 0     | Customer delivery city name.                                     |
| `customer_state`           | text      | 0     | Customer state abbreviation (e.g., SP, RJ).                      |

---

## 3. order_items

- **Grain:** One row per individual item contained within an order.
- **Key:** Composite Primary Key (`order_id`, `order_item_id`).
- **Total Rows:** 112,650
- **Links:** Links to `orders`, `products`, and `sellers`.

| Column Name           | Data Type | Nulls | Description & Notes                                                   |
| :-------------------- | :-------- | :---- | :-------------------------------------------------------------------- |
| `order_id`            | text      | 0     | Order identifier (Composite PK part 1).                               |
| `order_item_id`       | integer   | 0     | Sequential number of the item within the order (Composite PK part 2). |
| `product_id`          | text      | 0     | Product identifier (Foreign key to products).                         |
| `seller_id`           | text      | 0     | Seller identifier (Foreign key to sellers).                           |
| `shipping_limit_date` | timestamp | 0     | Max shipping limit date for the seller to dispatch the item.          |
| `price`               | float     | 0     | Item selling price (excludes freight).                                |
| `freight_value`       | float     | 0     | Item freight shipping cost.                                           |

---

## 4. order_payments

- **Grain:** One row per payment transaction/installment for an order.
- **Key:** Composite Primary Key (`order_id`, `payment_sequential`).
- **Total Rows:** 103,886
- **Links:** Links to `orders` (`order_id`).

| Column Name            | Data Type | Nulls | Description & Notes                                                             |
| :--------------------- | :-------- | :---- | :------------------------------------------------------------------------------ |
| `order_id`             | text      | 0     | Order identifier (Composite PK part 1).                                         |
| `payment_sequential`   | integer   | 0     | Sequence number of payment rows for multi-payment orders (Composite PK part 2). |
| `payment_type`         | text      | 0     | Method of payment (credit_card, boleto, voucher, debit_card).                   |
| `payment_installments` | integer   | 0     | Number of installments chosen for the payment.                                  |
| `payment_value`        | float     | 0     | Monetary value of the payment transaction.                                      |

- **payment_value:** payment_value includes the item prices and the freight. Some canceled orders have payments but no items. Vouchers are a way to pay, and they do not change price.

---

## 5. order_reviews

- **Grain:** One row per customer review submitted for an order.
- **Key:** Composite Primary Key (`review_id`, `order_id`).
- **Total Rows:** 99,224
- **Links:** Links to `orders` (`order_id`).

| Column Name               | Data Type | Nulls  | Description & Notes                                                       |
| :------------------------ | :-------- | :----- | :------------------------------------------------------------------------ |
| `review_id`               | text      | 0      | Unique review identifier (Composite PK part 1, can repeat across orders). |
| `order_id`                | text      | 0      | Order identifier (Composite PK part 2).                                   |
| `review_score`            | integer   | 0      | Customer satisfaction score from 1 to 5.                                  |
| `review_comment_title`    | text      | 87,656 | Title text of the customer review.                                        |
| `review_comment_message`  | text      | 58,247 | Detailed comment message left by the customer.                            |
| `review_creation_date`    | timestamp | 0      | Date when the review survey was sent/created.                             |
| `review_answer_timestamp` | timestamp | 0      | Timestamp when the survey response was answered.                          |

---

## 6. products

- **Grain:** One row per unique product catalog item.
- **Key:** `product_id` (32,951 unique values, Primary Key).
- **Total Rows:** 32,951
- **Links:** Links to `order_items` and `category_translation`.

| Column Name                  | Data Type | Nulls | Description & Notes                                      |
| :--------------------------- | :-------- | :---- | :------------------------------------------------------- |
| `product_id`                 | text      | 0     | Unique product identifier. Primary Key.                  |
| `product_category_name`      | text      | 610   | Category name in Portuguese.                             |
| `product_name_lenght`        | float     | 610   | Number of characters extracted from product name.        |
| `product_description_lenght` | float     | 610   | Number of characters extracted from product description. |
| `product_photos_qty`         | float     | 610   | Number of product photos published.                      |
| `product_weight_g`           | float     | 2     | Product weight measured in grams.                        |
| `product_length_cm`          | float     | 2     | Product length measured in centimeters.                  |
| `product_height_cm`          | float     | 2     | Product height measured in centimeters.                  |
| `product_width_cm`           | float     | 2     | Product width measured in centimeters.                   |

---

## 7. sellers

- **Grain:** One row per unique merchant/seller.
- **Key:** `seller_id` (3,095 unique values, Primary Key).
- **Total Rows:** 3,095
- **Links:** Links to `order_items` and `geolocation`.

| Column Name              | Data Type | Nulls | Description & Notes                             |
| :----------------------- | :-------- | :---- | :---------------------------------------------- |
| `seller_id`              | text      | 0     | Unique merchant identifier. Primary Key.        |
| `seller_zip_code_prefix` | text      | 0     | First 5 digits of seller zip code.              |
| `seller_city`            | text      | 0     | City where the seller operates.                 |
| `seller_state`           | text      | 0     | State abbreviation where the seller is located. |

---

## 8. category_translation

- **Grain:** One row per Portuguese-to-English category translation pair.
- **Key:** `product_category_name` (71 unique values, Primary Key).
- **Total Rows:** 71
- **Links:** Links to `products` (`product_category_name`).

| Column Name                     | Data Type | Nulls | Description & Notes                                |
| :------------------------------ | :-------- | :---- | :------------------------------------------------- |
| `product_category_name`         | text      | 0     | Original category name in Portuguese. Primary Key. |
| `product_category_name_english` | text      | 0     | Translated category name in English.               |

---

## 9. geolocation

- **Grain:** One row per zip code prefix coordinate coordinate entry.
- **Key:** No Primary Key (Many-to-many relationship due to overlapping zip code prefixes).
- **Total Rows:** 1,000,163
- **Links:** Links to `customers` and `sellers` via zip code prefix.

| Column Name                   | Data Type | Nulls | Description & Notes                    |
| :---------------------------- | :-------- | :---- | :------------------------------------- |
| `geolocation_zip_code_prefix` | text      | 0     | Zip code prefix.                       |
| `geolocation_lat`             | float     | 0     | Latitude coordinate.                   |
| `geolocation_lng`             | float     | 0     | Longitude coordinate.                  |
| `geolocation_city`            | text      | 0     | City name associated with coordinates. |
| `geolocation_state`           | text      | 0     | State abbreviation.                    |
