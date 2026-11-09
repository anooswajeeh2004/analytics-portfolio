## The question

What is wrong in the Olist data, and what should cleaning do about it?

## The answer

No real order is wrong enough to be completely removed from the dataset, as every recorded purchase represents a valid customer transaction.

| Problem                                                                               | Row Count    | Decision / Choice                                                 |
| ------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------- |
| Missing delivery dates (non-delivered statuses)                                       | 2,957 rows   | Kept in table; handled per specific delivery speed analysis.      |
| Missing delivery dates (delivered status)                                             | 8 rows       | Kept in table; flagged as anomaly without deletion.               |
| Look-alike item rows (same product multiple units)                                    | 10,225 rows  | Kept all rows; they represent real multiple quantities per order. |
| Chronological timeline violations (carrier before approval / delivery before carrier) | 1,382 rows   | Kept all orders; added `dates_ok` boolean flag column.            |
| Invalid payment records (no payment type & 0.00 value)                                | 3 rows       | Removed from dataset via cleaning log.                            |
| Invalid payment installments (0 installments)                                         | 2 rows       | Masked zero installments as missing (`NaN`).                      |
| Impossible product weight (0 grams)                                                   | 4 rows       | Masked zero weights as missing (`NaN`).                           |
| Unrealistic shipping deadline (> 365 days after purchase)                             | 1 row        | Masked deadline value as missing (`NaN`).                         |
| Non-city entries in location fields (zip codes, emails, state-only)                   | 7 rows       | Masked invalid text as missing (`NaN`).                           |
| Inconsistent city spellings                                                           | 33 spellings | Standardized via character normalization and regex rules.         |

Using a single blanket line of `dropna()` would have deleted 2,980 valid orders (3.0% of total volume), completely wiping out several order statuses (such as `shipped` and `invoiced`) and artificially dropping the observed cancellation rate from 0.63% to 0.01%.

## How sure I am

I am completely confident in removing zero-value non-payments, masking impossible zero weights/installments, and normalizing city text. I am moderately confident in flagging timeline violations rather than deleting rows, as preserving revenue and transaction counts is critical for analysis.

## What to do next

We should translate our defined cleaning rules into an automated python execution script for Day 8, ensuring that all transformations generate documented cleaning log entries for full auditability.
