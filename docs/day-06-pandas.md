# Day 6 — pandas, Past the Basics

## Part 0

### DataFrame Memory Comparison

| DataFrame  | Source / Change                                         | Memory (MB) |
| ---------- | ------------------------------------------------------- | ----------: |
| orders_csv | Raw CSV file                                            |        55.5 |
| orders     | PostgreSQL                                              |        25.9 |
| smaller    | PostgreSQL data with order_status converted to category |        20.2 |

Memory was measured using memory_usage(deep=True), including the index,
and converted to decimal megabytes.

### Purchase Timestamp Comparison

- CSV-loaded column: 6,761,988 bytes.
- PostgreSQL-loaded column: 795,528 bytes.
- Memory ratio: 8.5.

The purchase timestamp stored as text uses 8.5 times as much memory as
the datetime representation in this measurement.

### What I Learned

Data types affect DataFrame memory usage. Reading timestamps as real
datetimes reduced memory usage compared with text. Converting the
repeated order_status values to category reduced total memory further,
from 25.9 MB to 20.2 MB.

## Part 1

### Exercise 1.a — Matching Data Types

I copied orders_csv, converted the five timestamp columns to datetimes
using an explicit format, and converted order_status to category.

- Memory usage of fixed: 20.2 MB.
- fixed.equals(smaller): True.
- The original orders_csv was kept unchanged.

### Exercise 1.b — Categorical Storage

| Measurement                                               |          Before |           After |
| --------------------------------------------------------- | --------------: | --------------: |
| Customers DataFrame: state and city converted to category |         32.5 MB |         22.0 MB |
| customer_id column converted to category                  | 8,054,853 bytes | 8,452,617 bytes |

Converting repeated state and city values to category reduced memory usage.
However, customer_id did not get smaller because its values are unique:
categorical storage keeps all unique IDs plus a code for each row.

### Exercise 1.c — Nullable Integers

I converted the five remaining whole-number columns from float64 to Int64.

| Column                     | New type | Missing before | Missing after |
| -------------------------- | -------- | -------------: | ------------: |
| product_name_lenght        | Int64    |            610 |           610 |
| product_description_lenght | Int64    |            610 |           610 |
| product_length_cm          | Int64    |              2 |             2 |
| product_height_cm          | Int64    |              2 |             2 |
| product_width_cm           | Int64    |              2 |             2 |

The missing-value comparison returned True: missing-value counts stayed
unchanged across all columns.

### What I Learned

Category is useful for repeated labels, but it can increase memory usage
for unique IDs. Int64 represents whole numbers while preserving missing
values. Explicit datetime formats avoid ambiguous date interpretation.

## Part 2

### Merge Validation Error

First line of the error from the intentional items-to-payments merge:

> [Merge keys are not unique in right dataset; not a many-to-one merge]

The many_to_one validation failed because order_id is not unique in payments.
Without uniqueness validation, the merge repeats item rows for orders with
multiple payment records, which can inflate totals.

### Category Translation Matches

The products-to-translation left merge used many_to_one validation
and indicator=True.

| Merge indicator | Product count |
| --------------- | ------------: |
| both            |         32328 |
| left_only       |           623 |
| right_only      |             0 |

### Exercise 2.a — Payments to Orders

- Validation: many_to_one.
- Payment rows before the merge: 103,886.
- Rows after the inner merge: 103,886.

Multiple payment records can belong to one order. Every payment record
found a matching order, so no rows were lost or multiplied.

### Exercise 2.b — Orders Without Payment Records

I merged orders with payments using a left merge, one_to_many validation,
and indicator=True.

Filtering for left_only identified one order:

| order_id                         | order_status |
| -------------------------------- | ------------ |
| bfbd0f9bdef84302105ad712db648a6c | delivered    |

This order has no matching payment record in the dataset. Its delivered
status does not establish why the payment record is missing.

The order without a payment found in exercise 2.b is the exact same order identified in exercise 4.a of B9.

### Exercise 2.c — Missing Merge Keys

The inner merge of the two small example tables returned both rows.
The missing category matched the missing key in the right table and
received the label "No category".

A SQL INNER JOIN using ordinary equality would return only the toys row.
Pandas and SQL therefore handle missing join keys differently in this case.

### What I Learned

Validation checks whether merge keys satisfy the expected uniqueness
relationship. The merge indicator checks which rows found a match.
Both checks help detect problems before interpreting the results.

## Part 3

### Aggregation and Transformation

agg creates one summary row per order, while transform keeps every item
row and adds its group's result alongside it.

For order 06d5cbe68295558fd6c48998db3ea397, the example calculation is:

| order_item_id | price | order_total | pct_of_order |
| ------------- | ----: | ----------: | -----------: |
| 1             | 39.00 |      123.00 |         31.7 |
| 2             | 33.00 |      123.00 |         26.8 |
| 3             | 51.00 |      123.00 |         41.5 |

### Exercise 3.a — Items and Orders

- Item rows belonging to orders with at least two items: 23,787.
- Orders with at least two items: 9,803.

These counts measure different things: individual item rows versus
distinct orders.

### Exercise 3.b — Comparing Totals

| Calculation                        |    Total (R$) |
| ---------------------------------- | ------------: |
| Sum of repeated order_total values | 17,230,898.37 |
| Sum of individual item prices      | 13,591,643.70 |
| Sum of one items_total per order   | 13,591,643.70 |

The item-price sum matches the order-level summary sum.
Summing order_total across item rows overcounts because each order's
total appears once for every item in that order.

### Exercise 3.c — Tied Maximum Prices

The inspected order, 1b15974a0141d54e36626dca3fdc731a, contains 20 items,
each priced at R$100.00.

All 20 items share the maximum price, so all are kept in top_items.
This behaves like RANK() = 1 when ranking prices in descending order.
ROW_NUMBER() = 1 would keep only one row.

### What I Learned

The level of detail matters when counting or summing data.
A group total repeated by transform is useful for row-level comparisons,
but summing it again can inflate the result. Maximum-price filtering
also preserves ties, so it can return multiple items per order.

## Part 4

### Reshaping and Monthly Event Counts

I used melt to convert four timestamp columns into event rows, then
pivot_table to count each event by its own month.

| Month   | Purchased | Approved | To carrier | Delivered |
| ------- | --------: | -------: | ---------: | --------: |
| 2017-10 |     4,631 |    4,590 |      4,482 |     4,494 |
| 2017-11 |     7,544 |    7,395 |      6,637 |     4,670 |
| 2017-12 |     5,673 |    5,832 |      6,081 |     7,205 |

In November, purchases rose to 7,544, while recorded deliveries reached
4,670. In December, purchases fell to 5,673, while deliveries increased
to 7,205.

These counts use each event's own timestamp, so deliveries in a month
can belong to orders purchased in earlier months.

### Exercise 4.a — Missing Timestamps

There are 4,908 missing event timestamps across the dataset.

| Event      | Missing in events | Missing in original columns |
| ---------- | ----------------: | --------------------------: |
| purchased  |                 0 |                           0 |
| approved   |               160 |                         160 |
| to_carrier |             1,783 |                       1,783 |
| delivered  |             2,965 |                       2,965 |

The counts match before and after reshaping. melt preserved the missing
timestamps rather than removing their rows.

### Exercise 4.b — Payments by Purchase Month

I merged payments with order purchase timestamps using many_to_one
validation, then summed payment_value by purchase month and payment type.

| Purchase month | boleto (R$) | credit_card (R$) | debit_card (R$) | voucher (R$) |
| -------------- | ----------: | ---------------: | --------------: | -----------: |
| 2017-10        |  140,633.45 |       614,327.89 |        5,776.57 |    18,939.97 |
| 2017-11        |  226,292.34 |       942,856.67 |        6,168.10 |    19,565.69 |
| 2017-12        |  165,584.05 |       682,859.59 |        7,125.34 |    22,832.50 |

Credit cards accounted for the largest payment total in all three months.
The month refers to the order's purchase timestamp, not the payment
processing date. No order-status filter was applied.

### What I Learned

melt turns event columns into rows, making it easier to apply the same
operation to every event. pivot_table summarizes long data into a wide
table using an aggregation such as count or sum.

## Part 5

### Category Growth Analysis

I used one method chain to merge items with orders, products, and category
translations. Every merge used many_to_one validation.

The analysis counts item rows by purchase month, including all order
statuses. Categories must have at least 100 items in October 2017.
Growth is the November count divided by the October count.

The resulting table contains 18 categories. Its first three rows and
last row are:

| Category                 | October items | November items | Growth ratio |
| ------------------------ | ------------: | -------------: | -----------: |
| furniture_decor          |           379 |            783 |         2.07 |
| garden_tools             |           281 |            550 |         1.96 |
| fashion_bags_accessories |           110 |            200 |         1.82 |
| office_furniture         |           102 |            102 |         1.00 |

furniture_decor had the highest growth ratio among the qualifying
categories. office_furniture had unchanged item counts.

### Exercise 5.a — Overall Item Growth

| Purchase month | All item rows |
| -------------- | ------------: |
| 2017-10        |         5,322 |
| 2017-11        |         8,665 |

The overall growth ratio was approximately 1.63, meaning an increase
of approximately 62.8% in item count.

Of the 18 qualifying categories, 10 grew faster than all items combined.
This comparison used unrounded growth ratios.

### What I Learned

Method chaining keeps the analysis steps together in a readable sequence.
A growth ratio compares counts between months; it is not a percentage
increase or a measure of revenue.

The results describe observed changes but do not prove that Black Friday
caused those changes.

## Part 6

### Comparing Polars with Pandas

I rebuilt the category-growth table in Polars using the same months,
minimum October item count, and sorting rules as the pandas analysis.

The comparison returned (True, True):

- Category names matched in the same order.
- Rounded growth ratios matched in the same order.

### CSV Reading Performance

I measured the time needed to read olist_geolocation_dataset.csv three
times with each library.

| Run | Pandas (seconds) | Polars (seconds) | Pandas / Polars time ratio |
| --- | ---------------: | ---------------: | -------------------------: |
| 1   |             0.62 |             0.06 |                        9.9 |
| 2   |             0.65 |             0.07 |                        9.5 |
| 3   |             0.66 |             0.06 |                       10.5 |

Polars read the file approximately 9.5–10.5 times faster in these runs.
Ratios were calculated before rounding the displayed times.

These measurements cover CSV reading on this machine only. File caching
and system activity can affect the results; they do not establish the
speed of the complete analysis.

### Exercise 6.a — Join Validation Error

Changing the first join validation from m:1 to 1:1 produced:

> ComputeError: join keys did not fulfill 1:1 validation

The check failed because order_id repeats in the item records.
The appropriate relationship is many-to-one: multiple items can belong
to one order.

### When to Use Each Library

I would use pandas when its performance is sufficient and it fits the
existing workflow. I would try Polars when processing becomes too slow,
then verify its results against a trusted reference.

### What I Learned

Different libraries can produce matching analytical results while having
different performance characteristics. Join validation helps detect
incorrect assumptions about the data relationships.

## Errors and Lessons Learned

### Nullable Integer Conversion

Converting pd.Series([12.5, 3.0]) to Int64 raises a TypeError because
12.5 cannot be represented as an integer without changing its value.

Lesson: nullable integers preserve missing values and reject unsafe
conversion of fractional values. The intentional failing line is
commented out for the final notebook run.

### Pandas Merge Validation

The items-to-payments merge with many_to_one validation raises a
MergeError because order_id is not unique in payments.

Lesson: a successful merge without uniqueness checks can duplicate
item rows and inflate totals. The intentional failing line is
commented out for the final notebook run.

### Polars Join Validation

Changing the first join validation to 1:1 produced:

> ComputeError: join keys did not fulfill 1:1 validation

Lesson: multiple item rows can belong to the same order, so the
appropriate validation is m:1. The join must use m:1 in the final run.
