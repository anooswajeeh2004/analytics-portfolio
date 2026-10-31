# Data Dictionary Notes

## Table: order_items

- `price`: Represents the item sale price in BRL. Note: `price` does NOT include freight charges (`freight_value`).

## Table: order_payments

- `payment_value`: Total cash/value transferred for the order, which includes both item prices and freight costs.
- **Anomalies Note:** Some canceled orders may have payment entries without matching item entries in `order_items`.
- **Vouchers Note:** Vouchers act as a payment mechanism and do not alter the base product price in `order_items`.
