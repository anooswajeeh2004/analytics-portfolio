## The question

What does the cleaning pipeline change, and can we trust the clean tables?

## The answer

The cleaning pipeline removed 3 invalid payment rows, changed 282 rows across items, payments, products, sellers, and customers, and flagged 1,382 orders with chronological timeline anomalies without dropping them.

| Table          | Action  | Rows  | Rule                                              |
| -------------- | ------- | ----- | ------------------------------------------------- |
| customers      | changed | 226   | city spelling                                     |
| order_items    | changed | 4     | shipping deadline more than a year after purchase |
| order_payments | changed | 2     | 0 installments is impossible                      |
| order_payments | removed | 3     | no payment type and no money                      |
| orders         | flagged | 1,359 | carrier date before approval date                 |
| orders         | flagged | 23    | delivery date before carrier date                 |
| products       | changed | 4     | a weight of 0 g is impossible                     |
| sellers        | changed | 39    | city spelling                                     |
| sellers        | changed | 7     | not a city name                                   |

Specifically, data cleaning standardized city spellings for São Paulo (increasing its uniform seller count by resolving variations like `sao paulop`), and removed 3 zero-value non-payment records from the order payments table (reducing payment rows from 103,886 to 103,883).

## How sure I am

I am confident in the clean tables because all automated `pandera` validation schemas pass successfully before writing to PostgreSQL, ensuring strict data type and logical boundaries. However, checks cannot verify whether standardized city names reflect true underlying delivery addresses or detect unrecorded missing business transactions.

## What to do next

We should build downstream analytics and reporting pipelines directly against the `clean` database schema, relying on `clean.cleaning_log` for full transformation auditability.
