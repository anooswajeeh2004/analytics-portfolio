## Part 0

- **Error:** `NameError: name 'cleaned_payments' is not defined`
- **Teammate access:** To get the clean sellers today, a teammate must open your notebook and manually run all the preceding cleaning cells in the exact correct order.

## Part 1

### First Run Summary:

| Table          | Raw rows | Clean rows |
| -------------- | -------- | ---------- |
| orders         | 99,441   | 99,441     |
| order_items    | 112,650  | 112,650    |
| order_payments | 103,886  | 103,883    |
| products       | 32,951   | 32,951     |
| sellers        | 3,095    | 3,095      |
| customers      | 99,441   | 99,441     |
| order_reviews  | 99,224   | 99,224     |

| Table          | Action  | Rows | Rule                                              |
| -------------- | ------- | ---- | ------------------------------------------------- |
| customers      | changed | 226  | city spelling                                     |
| customers      | changed | 1    | not a city name                                   |
| order_items    | changed | 4    | shipping deadline more than a year after purchase |
| order_payments | changed | 2    | 0 installments is impossible                      |
| order_payments | removed | 3    | no payment type and no money                      |
| orders         | flagged | 1359 | carrier date before approval date                 |
| orders         | flagged | 23   | delivery date before carrier date                 |
| products       | changed | 4    | a weight of 0 g is impossible                     |
| sellers        | changed | 39   | city spelling                                     |
| sellers        | changed | 7    | not a city name                                   |

## Part 2

### Run Summary After Fixing the Rule:

| Table          | Raw rows | Clean rows |
| -------------- | -------- | ---------- |
| orders         | 99,441   | 99,441     |
| order_items    | 112,650  | 112,650    |
| order_payments | 103,886  | 103,883    |
| products       | 32,951   | 32,951     |
| sellers        | 3,095    | 3,095      |
| customers      | 99,441   | 99,441     |
| order_reviews  | 99,224   | 99,224     |

| Table          | Action  | Rows | Rule                                              |
| -------------- | ------- | ---- | ------------------------------------------------- |
| customers      | changed | 226  | city spelling                                     |
| order_items    | changed | 4    | shipping deadline more than a year after purchase |
| order_payments | changed | 2    | 0 installments is impossible                      |
| order_payments | removed | 3    | no payment type and no money                      |
| orders         | flagged | 1359 | carrier date before approval date                 |
| orders         | flagged | 23   | delivery date before carrier date                 |
| products       | changed | 4    | a weight of 0 g is impossible                     |
| sellers        | changed | 39   | city spelling                                     |
| sellers        | changed | 7    | not a city name                                   |

- **Rule Adjustment:** We updated the `not_a_city` condition in `clean_city` from `city.str.contains(r"[0-9@]")` to `city.str.fullmatch(r"[0-9]+") | city.str.contains("@")`. This ensures that only strings consisting entirely of digits (like zip codes) are flagged, rather than names containing numbers.
- **Analysis of `quilometro 14 do mutum`:** The original rule incorrectly flagged `quilometro 14 do mutum` because its name includes the number 14, even though it is a legitimate place in Espírito Santo. We found this false positive by inspecting the cleaning log in our notebook, which led us to refine the regular expression so it no longer misclassifies valid multi-word city names containing numbers.

## Part 3

### 1. Failures from Step 3 (Raw Payments Validation):

| column               | check                                                    | failure_case | index  |
| -------------------- | -------------------------------------------------------- | ------------ | ------ |
| payment_type         | isin(['credit_card', 'boleto', 'voucher', 'debit_card']) | not_defined  | 1612   |
| payment_type         | isin(['credit_card', 'boleto', 'voucher', 'debit_card']) | not_defined  | 2788   |
| payment_type         | isin(['credit_card', 'boleto', 'voucher', 'debit_card']) | not_defined  | 58230  |
| payment_installments | greater_than_or_equal_to(1)                              | 0            | 57221  |
| payment_installments | greater_than_or_equal_to(1)                              | 0            | 100771 |

### 2. Error from Step 5 (SchemaErrors Output):

```text
SchemaErrors: 
Failure cases:
  - column: payment_type
    check: isin(['credit_card', 'boleto', 'voucher', 'debit_card'])
    failure_case: ['not_defined', 'not_defined', 'not_defined']
    index: [1612, 2788, 58230]
```

3. The Three Schemas (Exercises 3.a, 3.b, 3.c):

**3.a products_schema:**

Python
products_schema = pa.DataFrameSchema(
{
"product_id": pa.Column(str, unique=True),
"product_weight_g": pa.Column("Int64", pa.Check.gt(0), nullable=True),
"category": pa.Column(str, nullable=False),
}
)

**3.b items_schema:**

Python
items_schema = pa.DataFrameSchema(
{
"price": pa.Column(float, pa.Check.gt(0)),
"freight_value": pa.Column(float, pa.Check.ge(0)),
},
unique=["order_id", "order_item_id"],
)

**3.c sellers_schema:**

Python
sellers_schema = pa.DataFrameSchema(
{
"seller_id": pa.Column(str, unique=True),
"seller_city": pa.Column(
str,
checks=[
pa.Check(lambda city: ~city.dropna().str.fullmatch(r"[0-9]+"), name="no digits only"),
pa.Check(lambda city: ~city.dropna().str.contains("@"), name="no @"),
],
nullable=True,
),
}
)

**Pipeline Summary with All Five Schemas:**

| Table          | Raw rows | Clean rows |
| -------------- | -------- | ---------- |
| orders         | 99,441   | 99,441     |
| order_items    | 112,650  | 112,650    |
| order_payments | 103,886  | 103,883    |
| products       | 32,951   | 32,951     |
| sellers        | 3,095    | 3,095      |
| customers      | 99,441   | 99,441     |
| order_reviews  | 99,224   | 99,224     |

| Table          | Action  | Rows | Rule                                              |
| -------------- | ------- | ---- | ------------------------------------------------- |
| customers      | changed | 226  | city spelling                                     |
| order_items    | changed | 4    | shipping deadline more than a year after purchase |
| order_payments | changed | 2    | 0 installments is impossible                      |
| order_payments | removed | 3    | no payment type and no money                      |
| orders         | flagged | 1359 | carrier date before approval date                 |
| orders         | flagged | 23   | delivery date before carrier date                 |
| products       | changed | 4    | a weight of 0 g is impossible                     |
| sellers        | changed | 39   | city spelling                                     |
| sellers        | changed | 7    | not a city name                                   |

## Errors seen today and lessons learned

1. **Error / Trap:** Executing cleaning transformations only inside Jupyter Notebook memory without persisting data.
   - **Lesson:** Notebook memory disappears upon kernel restart; an automated pipeline script (`clean.py`) writing to a database schema is essential for data persistence and team collaboration.

2. **Error / Trap:** Regex over-generalization on string columns (flagging `quilometro 14 do mutum` as non-city).
   - **Lesson:** `str.contains(r"[0-9]")` catches valid location names containing numbers. Using `str.fullmatch(r"[0-9]+")` ensures only entirely numeric strings like zip codes are masked.

3. **Error / Trap:** Data pipeline writing invalid data due to uncaught runtime schema violations.
   - **Lesson:** Integrating `pandera` validation schemas before database execution halts dirty data pipelines safely before corrupting existing clean database tables.
