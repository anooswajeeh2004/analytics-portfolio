| Rule                                              | Table                 | Rows                          | Action  | Why                                                                                                              |
| :------------------------------------------------ | :-------------------- | :---------------------------- | :------ | :--------------------------------------------------------------------------------------------------------------- |
| carrier date before approval date                 | orders                | 1,359                         | flagged | Chronological timeline error makes it impossible to know the exact wrong date, so we keep the order and flag it. |
| delivery date before carrier date                 | orders                | 23                            | flagged | Impossible sequence of delivery steps, so we flag the order to exclude it from time-gap calculations.            |
| shipping deadline more than a year after purchase | order_items           | 4                             | changed | Unrealistic shipping deadlines over a year are set to missing.                                                   |
| no payment type and no money                      | order_payments        | 3                             | removed | Incomplete payment records with zero value are not actual payments and get removed.                              |
| 0 installments is impossible                      | order_payments        | 2                             | changed | A payment must have at least 1 installment, so zero values are turned into missing.                              |
| a weight of 0 g is impossible                     | products              | 4                             | changed | Physical items must have weight, so 0 g entries are made missing.                                                |
| city spelling                                     | sellers and customers | 39 (sellers), 226 (customers) | changed | Standardizes diverse spelling variations and typos into a single uniform city name.                              |
| not a city name                                   | sellers and customers | 7 (sellers), 0 (customers)    | changed | Non-city entries like zip codes, emails, or state-only strings are masked as missing.                            |

### Non-removing choices:

1. **Missing values (Part 1):** Left missing because pandas safely skips `NaN` values in aggregations.
2. **Product categories with no English name (Part 1):** Given their English names using `EXTRA_TRANSLATIONS`, while categories with no name at all get `unknown`.
3. **Items that look like copies (Part 2):** Kept as distinct units since multiple quantities of the same product can exist in an order.
4. **Vouchers of 0.00 (exercise 3.d):** Kept as possible promotional or discount vouchers.
5. **Payments of orders with no items (exercise 3.e):** Kept as orphaned transactions.
6. **Canceled orders with a delivery date (exercise 3.f):** Kept as they are as orders might have been processed before cancellation notices.
