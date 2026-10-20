DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  order_id text,
  customer_id text,
  order_status text,
  order_purchase_timestamp timestamp,
  order_approved_at timestamp,
  order_delivered_carrier_date timestamp,
  order_delivered_customer_date timestamp,
  order_estimated_delivery_date timestamp
);
DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
  order_id text,
  order_item_id integer,
  product_id text,
  seller_id text,
  shipping_limit_date timestamp,
  price numeric(10, 2),
  freight_value numeric(10, 2)
);
-- 3. customers
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
  customer_id text,
  customer_unique_id text,
  customer_zip_code_prefix text,
  customer_city text,
  customer_state text
);
-- 4. geolocation
DROP TABLE IF EXISTS geolocation;
CREATE TABLE geolocation (
  geolocation_zip_code_prefix text,
  geolocation_lat numeric,
  geolocation_lng numeric,
  geolocation_city text,
  geolocation_state text
);
-- 5. order_payments
DROP TABLE IF EXISTS order_payments;
CREATE TABLE order_payments (
  order_id text,
  payment_sequential integer,
  payment_type text,
  payment_installments integer,
  payment_value numeric(10, 2)
);
-- 6. order_reviews
DROP TABLE IF EXISTS order_reviews;
CREATE TABLE order_reviews (
  review_id text,
  order_id text,
  review_score integer,
  review_comment_title text,
  review_comment_message text,
  review_creation_date timestamp,
  review_answer_timestamp timestamp
);
-- 7. products
DROP TABLE IF EXISTS products;
CREATE TABLE products (
  product_id text,
  product_category_name text,
  product_name_lenght integer,
  product_description_lenght integer,
  product_photos_qty integer,
  product_weight_g integer,
  product_length_cm integer,
  product_height_cm integer,
  product_width_cm integer
);
-- 8. sellers
DROP TABLE IF EXISTS sellers;
CREATE TABLE sellers (
  seller_id text,
  seller_zip_code_prefix text,
  seller_city text,
  seller_state text
);
-- 9. category_translation
DROP TABLE IF EXISTS category_translation;
CREATE TABLE category_translation (
  product_category_name text,
  product_category_name_english text
);