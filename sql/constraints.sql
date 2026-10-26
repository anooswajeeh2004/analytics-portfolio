ALTER TABLE
  orders
ADD
  PRIMARY KEY (order_id);
ALTER TABLE
  customers
ADD
  PRIMARY KEY (customer_id);
ALTER TABLE
  order_items
ADD
  PRIMARY KEY (order_id, order_item_id);
ALTER TABLE
  order_payments
ADD
  PRIMARY KEY (order_id, payment_sequential);
ALTER TABLE
  order_reviews
ADD
  PRIMARY KEY (review_id, order_id);
ALTER TABLE
  products
ADD
  PRIMARY KEY (product_id);
ALTER TABLE
  sellers
ADD
  PRIMARY KEY (seller_id);
ALTER TABLE
  category_translation
ADD
  PRIMARY KEY (product_category_name);
ALTER TABLE
  orders
ADD
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id);
ALTER TABLE
  order_items
ADD
  FOREIGN KEY (order_id) REFERENCES orders (order_id);
ALTER TABLE
  order_items
ADD
  FOREIGN KEY (product_id) REFERENCES products (product_id);
ALTER TABLE
  order_items
ADD
  FOREIGN KEY (seller_id) REFERENCES sellers (seller_id);
ALTER TABLE
  order_payments
ADD
  FOREIGN KEY (order_id) REFERENCES orders (order_id);
ALTER TABLE
  order_reviews
ADD
  FOREIGN KEY (order_id) REFERENCES orders (order_id);